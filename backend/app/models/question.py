from sqlalchemy import Column, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    question = Column(String, nullable=False)

    options = Column(JSON, nullable=False)

    answer = Column(String, nullable=False)

    explanation = Column(String)

    difficulty = Column(String)

    topic = Column(String)

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id"),
    )

    quiz = relationship(
        "Quiz",
        back_populates="questions",
    )