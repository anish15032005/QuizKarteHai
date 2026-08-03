from pathlib import Path
from typing import Any

from app.services.pdf_service import extract_text_from_pdf
from app.services.quiz_generation_service import generate_quiz_from_chunks
from app.utils.text_cleaner import clean_text
from app.utils.text_chunker import chunk_text


def process_pdf(file_path: Path) -> dict[str, Any]:
    """
    Complete PDF processing pipeline.

    Flow:
        PDF
          ↓
    Extract Text
          ↓
    Clean Text
          ↓
    Split into Chunks
          ↓
    Generate Quiz
    """

    pdf_data = extract_text_from_pdf(file_path)

    cleaned_text = clean_text(pdf_data["text"])

    chunks = chunk_text(cleaned_text)

    quiz = generate_quiz_from_chunks(chunks)

    return {
        "pages": pdf_data["pages"],
        "characters": len(cleaned_text),
        "chunk_count": len(chunks),
        "quiz": quiz,
    }