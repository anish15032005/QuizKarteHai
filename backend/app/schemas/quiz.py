from pydantic import BaseModel, Field


class QuizQuestion(BaseModel):
    question: str = Field(..., min_length=5)

    options: list[str] = Field(
        ...,
        min_length=4,
        max_length=4,
    )

    answer: str

    explanation: str | None = None

    difficulty: str = "Medium"

    topic: str | None = None