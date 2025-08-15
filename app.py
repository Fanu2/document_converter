import os
from pdf2docx import Converter
import pypandoc

def ensure_pandoc_installed():
    try:
        pypandoc.get_pandoc_version()
        print("Pandoc is already installed.")
    except OSError:
        print("Pandoc not found, downloading...")
        pypandoc.download_pandoc()
        print("Pandoc downloaded successfully.")

def convert_pdf_to_docx(pdf_path):
    output_path = f"{os.path.splitext(pdf_path)[0]}.docx"
    cv = Converter(pdf_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()
    return output_path

def convert_document(doc_file, target_format):
    try:
        ensure_pandoc_installed()
        target_format = target_format.lower()

        # Handle file-like or path input
        file_path = doc_file.name if hasattr(doc_file, 'name') else doc_file

        # Convert PDF to DOCX if needed
        if file_path.lower().endswith('.pdf'):
            print("Converting PDF to DOCX...")
            file_path = convert_pdf_to_docx(file_path)

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = f"converted_{base_name}.{target_format}"

        pypandoc.convert_file(file_path, target_format, outputfile=output_file)
        return output_file
    except Exception as e:
        print(f"Conversion error: {e}")
        return None
