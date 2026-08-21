import fitz
from docx import Document
import os 

def extract_pdf_text(file_path):
    text=""
    pdf=fitz.open(file_path)
    for page in pdf:
        text += page.get_text() + "\n"

    pdf.close()
    return text


def extract_docx_text(file_path):
    document = Document(file_path)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_txt_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def extract_text(file_path):

    if file_path.lower().endswith(".pdf"):
        return extract_pdf_text(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_docx_text(file_path)
    elif file_path.lower().endswith(".txt"):
        return extract_txt_text(file_path)  
    else:
        raise ValueError("Unsupported file format. Please provide a PDF, DOCX, or TXT file.")