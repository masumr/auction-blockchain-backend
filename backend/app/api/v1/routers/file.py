
import os
from typing import Optional
from fastapi import APIRouter, status, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse

from app.core.utils import file_upload, get_file_path

ALLOWED_FILE_EXTENSIONS = ["jpg", "jpeg", "png"]
IMAGE_UPLOAD_PATH = "media"


profile_router = pr = APIRouter()

@pr.post(
    "/upload_images/{address}",
    response_model_exclude_none=True,
    status_code=status.HTTP_202_ACCEPTED,
    
)
async def profile_image_upload(
        address: str,
        type: Optional[str] = "Profile", 
        file: UploadFile = File(...)
):
    upload_path = IMAGE_UPLOAD_PATH + f"/{type}"
    
    file_location = file_upload(file, address, upload_path, type)
    return "Successfully profile image uploaded"


@pr.get("/get_file_by_path/{address}", status_code=status.HTTP_200_OK, )
async def get_file(
        address: str,
        type: Optional[str] = "Profile"
):
    upload_path = IMAGE_UPLOAD_PATH + f"/{type}"
    file_path = get_file_path(address, upload_path, type)
    if not file_path:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {address} user's {type.lower()} image does not found!"
        )
    return FileResponse(file_path)
    
