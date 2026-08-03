from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.pdf_processing_service import process_pdf
from app.services.pdf_service import save_pdf
from app.services.quiz_service import create_quiz_with_questions

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"],
)


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    file_path = await save_pdf(file)

    result = process_pdf(file_path)

    quiz = create_quiz_with_questions(
        db=db,
        user_id=1,          # Temporary
        title=file.filename or "Untitled Quiz",
        questions=result["quiz"],
    )

    return {
        "quiz_id": quiz.id,
        "pages": result["pages"],
        "question_count": len(result["quiz"]),
    }