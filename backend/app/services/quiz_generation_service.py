from app.schemas.quiz import QuizQuestion
from app.services.ai_service import generate_mcqs
from app.utils.gemini_parser import parse_gemini_response


def generate_quiz_from_chunks(
    chunks: list[str],
) -> list[QuizQuestion]:
    """
    Generate quiz questions from text chunks using Gemini.
    """

    all_questions: list[QuizQuestion] = []

    print(f"Chunks received: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nProcessing chunk {index}/{len(chunks)}...")

        gemini_response = generate_mcqs(chunk)

        if gemini_response is None:
            print("Gemini returned no response.")
            continue

        try:
            parsed_response = parse_gemini_response(gemini_response)
        except Exception as e:
            print(f"JSON parsing failed: {e}")
            continue

        questions = parsed_response.get("questions", [])

        if not questions:
            print("No questions found in Gemini response.")
            continue

        for question in questions:
            try:
                validated_question = QuizQuestion(**question)
                all_questions.append(validated_question)
            except Exception as e:
                print(f"Question validation failed: {e}")

        print(f"Questions collected so far: {len(all_questions)}")

    print(f"\nTotal questions generated: {len(all_questions)}")

    return all_questions