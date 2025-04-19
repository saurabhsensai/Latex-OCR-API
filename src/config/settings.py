from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:3000"
    WORKERS: int = 4

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()