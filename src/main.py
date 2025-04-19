import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.api.endpoints import router as api_router
from src.utils.logging import setup_logging
from src.config.settings import settings
from contextlib import asynccontextmanager
import logging
# Load environment variables
load_dotenv()

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Equation to LaTeX API")
    yield
    logger.info("Shutting down Equation to LaTeX API")

# Initialize FastAPI app
app = FastAPI(
    title="Equation to LaTeX API",
    description="API to convert equation images to LaTeX code using pix2tex",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)

# Remove Uvicorn run from main block to avoid direct execution issues
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",  # Import string for multi-worker support
        host="0.0.0.0",
        port=settings.PORT,
        workers=settings.WORKERS,
        reload=False  # Disable reload for production
    )