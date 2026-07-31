from google import genai

from app.core.config import settings
from app.prompts.mcq_prompt import MCQ_PROMPT

client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)


def generate_mcqs(text: str, num_questions: int = 5):

    prompt = MCQ_PROMPT.format(
        text=text,
        num_questions=num_questions,
    )

    response = client.models.generate_content(
        model=settings.GOOGLE_MODEL,
        contents=prompt,
)

    return response.text