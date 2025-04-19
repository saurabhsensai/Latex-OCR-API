from fastapi import APIRouter, File, UploadFile, HTTPException
from src.schemas.response import LatexResponse
from src.models.equation_model import EquactionModel
from src.utils.image_processing import preprocess_image
import logging

router = APIRouter(prefix="/v1")
logger = logging.getLogger(__name__)


model = EquactionModel()

@router.post("/convert", response_model=LatexResponse)

async def convert_equaction(file: UploadFile=(File(...))):
    print("Hello 1")
    try: 
        print("Hello 2")
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, delail="Invalid File Type, Please upload an Image")
        
        contents = await file.read()
        image = preprocess_image(contents)

        result = model.predict(image)
        latex_code = result["latex"]
        confidence = result["confidence"]

        logger.info(f"Processed Image: {file.filename}")
        return LatexResponse(latex_code=latex_code, confidence=confidence)
    
    except Exception as e:
        logger.error(f"Error Processing Image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
    

@router.get("/health")

async def health_check():
    return {"status": "healthy"}



