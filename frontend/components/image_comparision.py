import streamlit as st
from backend.utils import create_download_link, get_image_dimensions
from io import BytesIO

def image_comparison_component(
    original_data: bytes,
    original_name: str,
    webp_buffer: BytesIO,
    webp_name: str,
    compression_ratio: float,
    quality: int
):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(original_data, use_column_width=True)
        original_size = len(original_data) / 1024  # KB
        width, height = get_image_dimensions(original_data)
        st.caption(f"""
            **{original_name}**  
            Dimensions: {width}×{height}  
            Size: {original_size:.2f} KB
        """)
    
    with col2:
        st.subheader("WebP Converted")
        st.image(webp_buffer, use_column_width=True)
        webp_size = len(webp_buffer.getvalue()) / 1024  # KB
        savings = (1 - (webp_size / original_size)) * 100
        st.caption(f"""
            **{webp_name}**  
            Quality: {quality}  
            Size: {webp_size:.2f} KB ({savings:.1f}% smaller)  
            Compression ratio: {compression_ratio:.2f}x
        """)
        
        st.markdown(
            create_download_link(webp_buffer, webp_name, "Download WebP"),
            unsafe_allow_html=True
        )
    
    st.markdown("---")