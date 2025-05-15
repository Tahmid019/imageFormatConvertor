from PIL import Image
from io import BytesIO
import os
from typing import Tuple, Optional
from .config import DEFAULT_QUALITY

class ImageConverter:
    @staticmethod
    def convert_to_webp(
        image_data: bytes,
        original_filename: str,
        quality: int = DEFAULT_QUALITY,
        optimize: bool = True
    ) -> Tuple[Optional[BytesIO], str, float]:
        """
        Convert image data to WebP format
        
        Args:
            image_data: Binary image data
            original_filename: Name of the original file
            quality: WebP quality (1-100)
            optimize: Whether to optimize the image
            
        Returns:
            Tuple containing:
            - BytesIO buffer with WebP data (or None if error)
            - New filename with .webp extension
            - Compression ratio (original_size/webp_size)
        """
        try:
            img = Image.open(BytesIO(image_data))
            
            # transparency for formats
            if img.mode == 'RGBA':
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            
            buffer = BytesIO()
            img.save(
                buffer,
                format="WEBP",
                quality=quality,
                optimize=optimize,
                method=6 #default
            )
            buffer.seek(0)
            
            filename, _ = os.path.splitext(original_filename)
            new_filename = f"{filename}.webp"
            
            # compression ratio
            original_size = len(image_data)
            webp_size = len(buffer.getvalue())
            compression_ratio = original_size / webp_size if webp_size > 0 else 1
            
            return buffer, new_filename, compression_ratio
            
        except Exception as e:
            raise ValueError(f"Image conversion failed: {str(e)}")