import streamlit as st
import fitz  # PyMuPDF
from fuzzywuzzy import fuzz
import json
import os
import base64
import nltk
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.docstore.document import Document
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd

# Download NLTK resources
nltk.download("punkt")

st.set_page_config(layout="wide")

# Directory paths
json_file_path = "C:\\Users\\VIKAS\\Desktop\\high\\sentences.json"

def read_pdf(file_path: str):
    file_docs = PyMuPDFLoader(file_path)
    file_docs = file_docs.load()
    combined_content = []
    for i, doc in enumerate(file_docs):
        combined_content.append( 
            Document(
                page_content = doc.page_content, 
            )
        )
    return combined_content

# Function to highlight sentences in the PDF
def highlight_pdf(pdf_path, sentences, output_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text("text")

        for sentence in sentences:
            tokenized_page_text = nltk.sent_tokenize(page_text)
            for page_sentence in tokenized_page_text:
                ratio = fuzz.ratio(sentence.lower(), page_sentence.lower())
                if ratio >= 70:  # Adjust the threshold as needed
                    words = page.search_for(page_sentence)
                    for word in words:
                        highlight = page.add_highlight_annot(word)
                        highlight.update()
                    break  # Break loop once a match is found

    # Save the highlighted PDF
    doc.save(output_path)
    doc.close()

# Streamlit app
st.title("PDF Sentence Highlighter")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    # Save uploaded file
    st.write("Data Loaded")
    file_name = uploaded_file.name
    base_name, ext = os.path.splitext(file_name)

    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    combined_text_data = read_pdf(file_path)

    try:
        with open(json_file_path, 'r') as f:
            sentences = json.load(f)
    except FileNotFoundError:
        st.error(f"The JSON file was not found in the directory: {json_file_path}")
        st.stop()

    sents = []
    reas = []
    for item in sentences:
        for key, value in item.items():
            sents.append(key)
            reas.append(value)

    # Highlight sentences in PDF
    save_path = os.path.join(os.getcwd(), base_name + "_highlighted.pdf")
    highlight_pdf(file_path, sents, save_path)

    with open(save_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1400" height="450" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    feedback_data = []
    feedback_list = []

    st.subheader("Provide Feedback for Each Reason")
    for dat in sentences:
        for key, value in dat.items():
            st.write(f'Line: **{key}**')
            st.write(f'Reasons: **{value}**')
            feedback = st.text_input(f"Feedback for: {key}", key=key)
            feedback_list.append({"Line": key, "Reason": value, "Feedback": feedback})

    feedback_df = pd.DataFrame(feedback_list)

    st.download_button(
        label="Download Feedback CSV",
        data=feedback_df.to_csv(index=False).encode('utf-8'),
        file_name="feedback.csv",
        mime="text/csv"
    )

    with open(save_path, "rb") as f:
        st.download_button(
            label="Download Highlighted PDF",
            data=f,
            file_name="highlighted.pdf",
            mime="application/pdf"
        )