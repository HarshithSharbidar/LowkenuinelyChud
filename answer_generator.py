def generate_answer(search_results, inferred_answers=None):

    if inferred_answers is None:
        inferred_answers = []

    # Display conclusions obtained through rule-based reasoning
    if inferred_answers:

        answer = "Answer derived through logical inference:\n\n"

        for inference in inferred_answers:

            answer += (
                "**Conclusion:** "
                + inference["conclusion"]
                + "\n\n"
            )

            answer += (
                "**Rule applied:** "
                + inference["rule"]
                + "\n\n"
            )

        return answer

    # Display retrieved document facts
    if not search_results:

        return (
            "Sorry, I could not find relevant information "
            "in the uploaded document."
        )

    best_results = search_results[:10]

    answer = "Based on the uploaded document:\n\n"

    for result in best_results:

        answer += "- " + result["sentence"] + "\n"

    return answer