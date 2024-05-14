from pdfreader import SimplePDFViewer
from docx import Document
#from google.colab import files, drive
import os

def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        viewer = SimplePDFViewer(file)
        text_elements = []
        for canvas in viewer:
            if canvas.strings:
                text_elements.extend(canvas.strings)
        text = "\n".join(text_elements)
    return text

def read_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_files_in_directory(directory):
    files_data = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".pdf"):
            text = read_pdf(file_path)
        elif filename.endswith(".docx"):
            text = read_docx(file_path)
        elif filename.endswith(".txt"):
            text = read_txt(file_path)
        else:
            continue
        #text = preprocess_text(text)
        files_data.append([filename, text])
    return files_data