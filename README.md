PDF Sentence Highlighter

Overview:
This project is a web application built with Streamlit that allows users to upload a PDF file, highlight specific sentences based on a provided JSON file, 
and download the highlighted PDF and feedback in CSV format. It leverages libraries such as PyMuPDF, NLTK, and fuzzywuzzy for text processing and highlighting.

Features:
Upload PDF: Users can upload a PDF file from their device.
Highlight Sentences: Sentences specified in a JSON file are highlighted in the uploaded PDF.
View and Download PDF: Users can view the highlighted PDF directly in the app and download it.
Provide Feedback: Users can provide feedback on highlighted sentences.
Download Feedback: The feedback can be downloaded as a CSV file for further analysis.

Technologies Used :
Streamlit: Framework for building the web application.
PyMuPDF (fitz): Library for reading and manipulating PDF files.
NLTK: Library for natural language processing, specifically for sentence tokenization.
fuzzywuzzy: Library for fuzzy string matching to handle minor differences in text.
pandas: Library for handling and exporting feedback data.

Installation:
To set up and run the application locally, follow these steps:
Clone the Repository

git clone https://github.com/navdeep7880/PDF-Highlighter
Navigate to the Project Directory

cd pdf-sentence-highlighter
Create and Activate a Virtual Environment

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Install Required Packages

pip install -r requirements.txt
Run the Streamlit Application

streamlit run app.py
Usage
Upload a PDF File: Click on the "Upload a PDF file" button to select and upload your PDF.

Provide JSON File: Ensure a JSON file containing the sentences to be highlighted is available. The JSON file should be formatted as follows:

json
Copy code
[
    {"Sentence to Highlight": "Reason for highlighting"},
    {"Another sentence": "Another reason"}
]
View Highlighted PDF: Once the PDF is processed, the highlighted PDF will be displayed in the app. You can view and download it.

Provide Feedback: Enter feedback for each highlighted sentence in the provided input fields.

Download Feedback: Download the CSV file containing your feedback by clicking the "Download Feedback CSV" button.

Files :

app.py: Main application file containing the Streamlit code.
requirements.txt: List of Python dependencies for the project.
sentences.json: Example JSON file format (not included; you need to create this file with your data).
Contributing
Feel free to fork the repository, make changes, and submit a pull request. Contributions are welcome!


Acknowledgements
Streamlit: For providing an easy-to-use framework for creating web applications.
PyMuPDF: For enabling PDF manipulation.
NLTK: For natural language processing tools.
fuzzywuzzy: For fuzzy string matching capabilities.
pandas: For data handling and exporting.
