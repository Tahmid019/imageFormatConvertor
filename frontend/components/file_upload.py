import streamlit as st
from backend.config import MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS

def file_uploader_component(settings: dict):
    uploaded_files = st.file_uploader(
        "Upload images to convert",
        type=ALLOWED_EXTENSIONS,
        accept_multiple_files=True,
        help=f"Maximum file size: {MAX_FILE_SIZE_MB}MB"
    )
    
    if uploaded_files:
        valid_files = []
        for file in uploaded_files:
            file_size_mb = len(file.getvalue()) / (1024 * 1024)
            if file_size_mb > MAX_FILE_SIZE_MB:
                st.warning(f"File {file.name} is too large ({file_size_mb:.2f}MB). Skipping.")
            else:
                valid_files.append(file)
                
        return valid_files
    return None