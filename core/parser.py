import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):

    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    with zipfile.ZipFile(docx_path) as docx_zip:

        xml_content = docx_zip.read('word/document.xml')

    root = ET.fromstring(xml_content)

    all_text = []

    for p_tag in root.findall('.//w:p', ns):
        text_pieces = []
        for t_tag in p_tag.findall('.//w:t', ns):
            if t_tag.text:
                text_pieces.append(t_tag.text)

        full_text = "".join(text_pieces)
        if full_text.strip():  # Only add non-empty all_text
            all_text.append(full_text)

    return "\n".join(all_text)

def extract_text_from_pptx(file_path):
    ns = {'a': 'http://openxmlformats.org',
          'p': 'http://openxmlformats.org'}
    all_text = []
    with zipfile.ZipFile(file_path, 'r') as pptx_zip:
        slide_files = [f for f in pptx_zip.namelist() if f.startswith('ppt/slides/slide')]
        for slide_file in sorted(slide_files):
            xml_content = pptx_zip.read(slide_file)
            root = ET.fromstring(xml_content)
            for t_tag in root.findall('.//a:t', ns):
                if t_tag.text:
                    all_text.append(t_tag.text)
    return "\n".join(all_text)


# test running code

if __name__ == "__main__":
    print("Running test code for extract_text_from_docx function...")

    try :
        docx_text = extract_text_from_docx("datasets/test.docx")
        print(docx_text)
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n --test pptx scratch parser   --")
    try:
        pptx_text = extract_text_from_pptx("datasets/test.pptx")
        print(pptx_text)
    except Exception as e:
        print(f"An error occurred: {e}")