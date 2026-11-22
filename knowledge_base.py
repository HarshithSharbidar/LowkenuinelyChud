import re


STOPWORDS = {
    "the", "is", "are", "was", "were", "a", "an",
    "and", "or", "but", "to", "of", "in", "on",
    "for", "with", "by", "at", "from", "as",
    "it", "this", "that", "these", "those",
    "what", "who", "when", "where", "why", "how",
    "does", "do", "did", "can", "could", "would",
    "should", "which", "about", "explain", "tell",
    "me", "please", "happens", "done"
}


class KnowledgeBase:

    def __init__(self):
        self.facts = []

    def add_facts(self, sentences):

        self.facts = []

        for sentence in sentences:

            if re.search(
                r'\bif\b.*\bthen\b',
                sentence,
                re.IGNORECASE
            ):
                continue

            words = re.findall(
                r'\b[a-zA-Z0-9]+\b',
                sentence.lower()
            )

            keywords = {
                word for word in words
                if word not in STOPWORDS and len(word) > 1
            }

            if keywords:

                self.facts.append({
                    "sentence": sentence,
                    "keywords": keywords
                })

    def search(self, question):

        question_words = re.findall(
            r'\b[a-zA-Z0-9]+\b',
            question.lower()
        )

        question_keywords = {
            word for word in question_words
            if word not in STOPWORDS and len(word) > 1
        }

        if not question_keywords:
            return []

        scored_facts = []

        for index, fact in enumerate(self.facts):

            common_words = (
                question_keywords & fact["keywords"]
            )

            score = (
                len(common_words) /
                len(question_keywords)
            )

            if score > 0:

                scored_facts.append({
                    "index": index,
                    "score": score
                })

        if not scored_facts:
            return []

        scored_facts.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        # Identify the strongest matching sentence
        best_index = scored_facts[0]["index"]

        # Retrieve nearby sentences to preserve context
        start = max(0, best_index - 1)
        end = min(len(self.facts), best_index + 11)

        results = []

        for index in range(start, end):

            results.append({
                "sentence": self.facts[index]["sentence"],
                "score": 1.0 if index == best_index else 0.5
            })

        return results