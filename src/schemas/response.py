from pydantic import BaseModel
from typing import Optional

class LatexResponse(BaseModel):
    latex_code: str
    confidence: Optional[float] = None
    error: Optional[str] = None
