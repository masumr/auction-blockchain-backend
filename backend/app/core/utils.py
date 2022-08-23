import os
import base64
import shutil
from typing import List
from fastapi import status, HTTPException, UploadFile
from fastapi.responses import FileResponse

ALLOWED_FILE_EXTENSIONS = ["jpg", "jpeg", "png"]


def encoding_base64_string(value: str) -> str:
    value_bytes = value.encode("ascii")
    base64_bytes = base64.b64encode(value_bytes)
    base64_value = base64_bytes.decode("ascii")
    return base64_value


def decoding_base64_string(base64_value: str) -> str:
    base64_bytes = base64_value.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    value = message_bytes.decode("ascii")
    return value


def file_upload(
        file: UploadFile,
        address: str,
        upload_path: str,
        ALLOWED_FILE_EXTENSIONS: List = ALLOWED_FILE_EXTENSIONS,
) -> str:
    filename = file.filename
    split_file_name = os.path.splitext(filename)
    file_extension = split_file_name[1].split(".")[-1]
    if file_extension.lower() not in ALLOWED_FILE_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"File type must be one of {', '.join(ALLOWED_FILE_EXTENSIONS)}",
        )
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    new_name = f"{encoding_base64_string(address)}.{file_extension}"
    file_location = f"{upload_path}/{new_name}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_location

def get_file_path(address: str, upload_path: str, type: str):
    path = encoding_base64_string(address)
    for _extenstion in ALLOWED_FILE_EXTENSIONS:
        path_dir = "{}/{}".format(
            # os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            upload_path,
            f"{path}.{_extenstion}"
        )
        print(path_dir)
        if os.path.exists(path_dir):
            return FileResponse(path_dir)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {address} user's {type.lower()} image does not found!"
        )