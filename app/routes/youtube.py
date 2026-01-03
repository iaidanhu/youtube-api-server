from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.models.youtube import YouTubeRequest
from app.utils.youtube_tools import YouTubeTools

router = APIRouter(
    prefix="/youtube",
    tags=["youtube"],
    responses={404: {"description": "Not found"}},
)

# Create a limiter for this router
limiter = Limiter(key_func=get_remote_address)

@router.post("/video-data")
@shared_limiter.limit("10/minute")
async def get_video_data(request: Request, youtube_request: YouTubeRequest):
    """Endpoint to get video metadata"""
    return YouTubeTools.get_video_data(youtube_request.url)

@router.post("/video-captions")
@shared_limiter.limit("10/minute")
async def get_video_captions(request: Request, youtube_request: YouTubeRequest):
    """Endpoint to get video captions"""
    return YouTubeTools.get_video_captions(youtube_request.url, youtube_request.languages)

@router.post("/video-timestamps")
@shared_limiter.limit("10/minute")
async def get_video_timestamps(request: Request, youtube_request: YouTubeRequest):
    """Endpoint to get video timestamps"""
    return YouTubeTools.get_video_timestamps(youtube_request.url, youtube_request.languages)