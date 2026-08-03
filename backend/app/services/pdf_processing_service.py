from pathlib import Path
from typing import Any

from app.services.pdf_service import extract_text_from_pdf


def process_pdf(file_path: Path):

    pdf_data: dict[str, Any] = extract_text_from_pdf(file_path)

    return {
        "pages": pdf_data["pages"],
        "characters": len(pdf_data["text"]),
        "preview": pdf_data["text"][:500],
        "text": pdf_data["text"],
    }