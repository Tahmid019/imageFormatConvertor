import streamlit as st
from backend.convertor import ImageConverter
from backend.utils import create_download_link, get_image_dimensions
from backend.config import DEFAULT_QUALITY, MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS
from frontend.components.sidebar import show_sidebar
from frontend.components.file_upload import file_uploader_component
from frontend.components.image_comparision import image_comparison_component
import os
from io import BytesIO

with open(os.path.join(os.path.dirname(__file__), "assets", "logoSvg.svg")) as logos:
    logo_svg = logos.read()

def main():
    st.set_page_config(
        page_title="Advanced WebP Converter",
        page_icon=logo_svg,
        layout="wide"
    )
    
    with open(os.path.join(os.path.dirname(__file__), "assets", "styles.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.title("Image to WebP Converter")
    st.markdown("""
        Convert your JPG, JPEG, or PNG images to WebP format with adjustable quality settings.
        WebP typically provides better compression than traditional formats while maintaining similar quality.
    """)
    
    settings = show_sidebar()
    
    uploaded_files = file_uploader_component(settings)
    
    if uploaded_files:
        st.subheader("Conversion Results")
        
        for uploaded_file in uploaded_files:
            file_data = uploaded_file.getvalue()
            
            try:
                webp_buffer, new_filename, compression_ratio = ImageConverter.convert_to_webp(
                    file_data,
                    uploaded_file.name,
                    quality=settings['quality'],
                    optimize=settings['optimize']
                )
                
                image_comparison_component(
                    original_data=file_data,
                    original_name=uploaded_file.name,
                    webp_buffer=webp_buffer,
                    webp_name=new_filename,
                    compression_ratio=compression_ratio,
                    quality=settings['quality']
                )
                
            except Exception as e:
                st.error(f"Failed to convert {uploaded_file.name}: {str(e)}")

if __name__ == "__main__":
    main()