MCQ_PROMPT = """
You are an expert teacher.

Generate exactly {num_questions} multiple-choice questions from the following study material.

Requirements:
- Return ONLY valid JSON.
- Do not write markdown.
- Do not wrap the response inside ```.

JSON format:

{
  "questions": [
    {
      "question": "...",
      "options": [
        "...",
        "...",
        "...",
        "..."
      ],
      "answer": "...",
      "explanation": "..."
    }
  ]
}

Study Material:

{text}
"""