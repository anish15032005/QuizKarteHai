from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.quiz import Quiz
from app.schemas.quiz import QuizQuestion


def create_quiz_with_questions(
    db: Session,
    user_id: int,
    title: str,
    questions: list[QuizQuestion],
) -> Quiz:
    """
    Create a quiz and all of its questions
    in a single database transaction.
    """

    quiz = Quiz(
        title=title,
        user_id=user_id,
    )

    db.add(quiz)

    db.flush()

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

    db.refresh(quiz)

    return quiz