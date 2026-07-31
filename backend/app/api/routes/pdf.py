from fastapi import APIRouter, File, UploadFile

from app.services.pdf_service import (
    save_pdf,
    extract_text_from_pdf,
)

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"],
)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = await save_pdf(file)

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "pages_text_length": len(extracted_text),
        "preview": extracted_text[:500],
    }