from pix2tex.cli import LatexOCR
from PIL import Image


class EquactionModel:
    def __init__(self):
        self.model = LatexOCR()
        print("Model Initialized")
    
    def predict(self, image: Image.Image) -> dict:
        latex_code = self.model(image)
        return {"latex": latex_code, "confidence": None}


