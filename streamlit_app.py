import streamlit as st
import pypandoc
import os

# Ensure Pandoc is available
try:
    pypandoc.get_pandoc_path()
except OSError:
    with st.spinner("Downloading Pandoc..."):
        pypandoc.download_pandoc()

st.set_page_config(page_title="Document Converter", layout="centered")
st.title("📄 Document Converter")

# Supported formats
input_formats = ["docx", "odt", "html", "md", "txt"]
output_formats = ["pdf", "docx", "html", "md", "txt"]

uploaded_file = st.file_uploader("Upload a document", type=input_formats)
output_format = st.selectbox("Convert to format", output_formats)

if uploaded_file and output_format:
    input_path = f"temp_input.{uploaded_file.name.split('.')[-1]}"
    output_path = f"converted.{output_format}"

    # Save uploaded file
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    try:
        # Convert using Pandoc
        pypandoc.convert_file(input_path, output_format, outputfile=output_path)
        st.success(f"✅ Converted to {output_format}!")

        # Offer download
        with open(output_path, "rb") as f:
            st.download_button(
                label="📥 Download Converted File",
                data=f,
                file_name=output_path,
                mime="application/octet-stream"
            )
    except Exception as e:
        st.error(f"❌ Conversion failed: {e}")

    # Clean up
    os.remove(input_path)
    if os.path.exists(output_path):
        os.remove(output_path)
