import re


def clean_text(text: str) -> str:

    # Remove multiple blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    # Replace multiple spaces with one
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text