import json


def parse_gemini_response(response: str):
    """
    Convert Gemini's response into a Python object.
    Removes markdown code fences if present.
    """

    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    return json.loads(response)