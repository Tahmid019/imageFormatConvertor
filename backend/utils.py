import base64
from typing import Tuple
from io import BytesIO

def get_image_dimensions(image_data: bytes) -> Tuple[int, int]:
    from PIL import Image
    with Image.open(BytesIO(image_data)) as img:
        return img.size

def create_download_link(
    buffer: BytesIO,
    filename: str,
    link_text: str = "Download"
) -> str:
    b64 = base64.b64encode(buffer.getvalue()).decode()
    return f'<a href="data:file/webp;base64,{b64}" download="{filename}">{link_text}</a>'

def validate_image_file(file_data: bytes, allowed_formats: tuple = ('JPEG', 'PNG')) -> bool:
    from PIL import Image
    try:
        with Image.open(BytesIO(file_data)) as img:
            return img.format in allowed_formats
    except:
        return False