import os
from pypdf import PdfReader
from docx import Document
from pptx import Presentation
import openpyxl

def stream_pdf(file_path):
    reader = PdfReader(file_path)
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            for p in text.split("\n\n"):
                if len(p.strip()) > 20:
                    yield (p.strip(), f"Page {page_num + 1}")


def stream_docx(file_path):
    doc = Document(file_path)
    idx = 1
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if len(text) > 20:
            sentences = text.split('. ')
            for sentence in sentences:
                s_clean = sentence.strip()
                if len(s_clean) > 15:
                    yield (s_clean, f"Paragraph {idx}")
            idx += 1


def stream_pptx(file_path):
    prs = Presentation(file_path)
    for slide_idx, slide in enumerate(prs.slides):
        for shape in slide.shapes:
            if hasattr(shape, "text") and shape.text.strip():
                text = shape.text.strip()
                if len(text) > 20:
                    yield (text, f"Slide {slide_idx + 1}")

def stream_excel(file_path):
    wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        for row_idx, row in enumerate(sheet.iter_rows(values_only=True)):
            
            row_text = " ".join([str(cell) for cell in row if cell is not None]).strip()
            if len(row_text) > 20:
                yield (row_text, f"Sheet: {sheet_name}, Row {row_idx + 1}")

def stream_any_document(file_path):
    """
    Main Manager Function: Ye automatic extension detect karke 
    bina memory crash kiye chunks yield karega.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    ext = file_path.split('.')[-1].lower()
    
    if ext == 'pdf':
        yield from stream_pdf(file_path)
    elif ext in ['docx', 'doc']:
        yield from stream_docx(file_path)
    elif ext in ['pptx', 'ppt']:
        yield from stream_pptx(file_path)
    elif ext in ['xlsx', 'xls']:
        yield from stream_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: .{ext}")
