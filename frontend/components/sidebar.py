import streamlit as st
from backend.config import DEFAULT_QUALITY

def show_sidebar() -> dict:
    with st.sidebar:
        st.header("Conversion Settings")
        
        settings = {
            'quality': st.slider(
                "WebP Quality",
                min_value=1,
                max_value=100,
                value=DEFAULT_QUALITY,
                help="Higher values mean better quality but larger files"
            ),
            'optimize': st.checkbox(
                "Optimize Image",
                value=True,
                help="Enable optimization for smaller file sizes"
            ),
            'preserve_metadata': st.checkbox(
                "Preserve Metadata",
                value=False,
                help="Keep EXIF and other metadata (may increase file size)"
            )
        }
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
            WebP is a modern image format that provides superior lossless and lossy 
            compression for images on the web.
            
            - Typically 25-35% smaller than JPEG at similar quality
            - Supports transparency like PNG
            - Supported by all modern browsers
        """)
        
    return settings