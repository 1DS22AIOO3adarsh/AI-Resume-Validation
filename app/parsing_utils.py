import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set the path if Windows install is not in PATH

from pdf2image import convert_from_path
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    if len(text.strip()) > 500:
        return text
    
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
