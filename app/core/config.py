import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Application settings
    
    Reads settings from environment variables or .env file
    """
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "YouTube Tools API"
    
    # Server settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # CORS settings - specify allowed origins in production
    BACKEND_CORS_ORIGINS: list = [origin.strip() for origin in os.getenv("BACKEND_CORS_ORIGINS", "*").split(",")]
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Proxy settings
    PROXY_USERNAME: str = os.getenv("PROXY_USERNAME")
    PROXY_PASSWORD: str = os.getenv("PROXY_PASSWORD")
    
    # Rate limiting
    RATE_LIMIT: str = os.getenv("RATE_LIMIT", "20/minute")
    
    # Cache settings
    CACHE_DEFAULT_TTL: int = int(os.getenv("CACHE_DEFAULT_TTL", "3600"))

# Create settings instance
settings = Settings()