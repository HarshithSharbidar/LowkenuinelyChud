import re

QUESTION_TYPES = {
    "who": "person",
    "when": "time",
    "where": "location",
    "why": "reason",
    "how": "method",
    "what": "definition"
}


def process_question(question):

    question = question.strip()

    if not question:
        return None

    words = re.findall(
        r'\b[a-zA-Z0-9]+\b',
        question.lower()
    )

    question_type = "general"

    for word in words:
        if word in QUESTION_TYPES:
            question_type = QUESTION_TYPES[word]
            break

    return {
        "original_question": question,
        "keywords": words,
        "question_type": question_type
    }