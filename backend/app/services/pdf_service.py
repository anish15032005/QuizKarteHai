from pathlib import Path
import shutil

import fitz
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


async def save_pdf(file: UploadFile):
    if not file.filename:
        raise ValueError("Uploaded file must have a filename")
    if file.content_type != "application/pdf":
        raise ValueError("Only PDF files are allowed.")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


def extract_text_from_pdf(file_path: Path):

    document = fitz.open(file_path)

    text_parts = []

    for page in document:
        text_parts.append(page.get_text())

    text = "\n".join(text_parts)

    pages = len(document)

    document.close()

    return {
        "pages": pages,
        "text": text,
    }