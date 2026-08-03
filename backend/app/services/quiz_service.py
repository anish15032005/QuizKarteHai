#backend/app/services/quiz_service.py

from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.quiz import Quiz
from app.schemas.quiz import QuizQuestion


def create_quiz(
    db: Session,
    title: str,
    user_id: int,
) -> Quiz:
    """
    Create a new quiz.
    """

    quiz = Quiz(
        title=title,
        user_id=user_id,
    )

    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    return quiz


def save_questions(
    db: Session,
    quiz: Quiz,
    questions: list[QuizQuestion],
) -> None:
    """
    Save all questions belonging to a quiz.
    """

    for question in questions:

        db_question = Question(
            question=question.question,
            options=question.options,
            answer=question.answer,
            explanation=question.explanation,
            difficulty=question.difficulty,
            topic=question.topic,
            quiz_id=quiz.id,
        )

        db.add(db_question)

    db.commit()