from pathlib import Path
import shutil
from fastapi import UploadFile

# Folder where uploaded PDFs will be stored
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


async def save_pdf(file: UploadFile):
    if not file.filename:
        raise ValueError("Uploaded file must have a filename")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path