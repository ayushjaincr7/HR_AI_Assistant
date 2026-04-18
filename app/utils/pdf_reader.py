from PyPDF2 import PdfReader

def extract_text_from_pdf(upload_file):
    reader = PdfReader(upload_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text.strip()