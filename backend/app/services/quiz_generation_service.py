from app.services.ai_service import generate_mcqs


def generate_quiz_from_chunks(chunks):

    questions = []

    for chunk in chunks:

        response = generate_mcqs(chunk)

        questions.append(response)

    return questions