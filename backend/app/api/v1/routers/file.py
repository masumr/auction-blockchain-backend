from audioop import add
import os
from re import I
from fastapi import APIRouter, status, File, UploadFile, HTTPException, status

from app.core.utils import file_upload, get_file_path

ALLOWED_FILE_EXTENSIONS = ["jpg", "jpeg", "png"]
IMAGE_UPLOAD_PATH = "media/profile"


profile_router = pr = APIRouter()

@pr.post(
    "/upload_images/{address}",
    response_model_exclude_none=True,
    status_code=status.HTTP_202_ACCEPTED,
    
)
async def profile_image_upload(
        address: str,
        file: UploadFile = File(...)
):
    file_location = file_upload(file, address, IMAGE_UPLOAD_PATH)
    return "Successfully profile image uploaded"

@pr.get("/get_file_by_path/{address}", status_code=status.HTTP_200_OK, )
async def get_file(
        address: str
):
    return get_file_path(address, IMAGE_UPLOAD_PATH)
    
