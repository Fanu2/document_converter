import gradio as gr
from converter import convert_document
import pypandoc

# Supported formats
input_formats = sorted(pypandoc.get_pandoc_formats()[0])
output_formats = sorted(pypandoc.get_pandoc_formats()[1])
input_formats.append("PDF")  # Manual addition

interface = gr.Interface(
    fn=convert_document,
    inputs=[
        gr.File(label="Upload Document", file_types=[f".{fmt.lower()}" for fmt in input_formats]),
        gr.Dropdown(label="Select Output Format", choices=[fmt.upper() for fmt in output_formats])
    ],
    outputs=gr.File(label="Converted Document"),
    title="Document Format Converter",
    description="Upload a document and choose a format to convert to.",
    css="footer {visibility: hidden}"
)

if __name__ == "__main__":
    interface.launch()
