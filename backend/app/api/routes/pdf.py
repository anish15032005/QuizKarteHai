from fastapi import APIRouter, File, UploadFile

from app.services.pdf_service import save_pdf

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"],
)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = await save_pdf(file)

    return {
        "message": "Upload successful",
        "filename": file.filename,
        "saved_to": str(file_path),
    }