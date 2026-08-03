from typing import List


def chunk_text(text: str, chunk_size: int = 12000) -> List[str]:
    """
    Split text into chunks suitable for Gemini.
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start = end

    return chunks