from PIL import Image
import io

def preprocess_image(image_bytes: bytes) -> Image.Image:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return image