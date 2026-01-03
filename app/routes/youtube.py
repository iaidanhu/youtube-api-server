from fastapi import APIRouter, Request

from app.models.youtube import YouTubeRequest
from app.utils.youtube_tools import YouTubeTools

router = APIRouter(
    prefix="/youtube",
    tags=["youtube"],
    responses={404: {"description": "Not found"}},
)

@router.post("/video-data")
async def get_video_data(request: Request, youtube_request: YouTubeRequest):
    """Endpoint to get video metadata"""
    # Apply rate limiting
    await request.app.state.limiter.__call__(request)
    return YouTubeTools.get_video_data(youtube_request.url)

@router.post("/video-captions")
async def get_video_captions(request: Request, youtube_request: YouTubeRequest):
    """Endpoint to get video captions"""
    # Apply rate limiting
    await request.app.state.limiter.__call__(request)
    return YouTubeTools.get_video_captions(youtube_request.url, youtube_request.languages)

@router.post("/video-timestamps")
async def get_video_timestamps(request: Request, youtube_request: YouTubeRequest):
    """Endpoint to get video timestamps"""
    # Apply rate limiting
    await request.app.state.limiter.__call__(request)
    return YouTubeTools.get_video_timestamps(youtube_request.url, youtube_request.languages)