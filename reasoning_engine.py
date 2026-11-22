import re


STOPWORDS = {
    "the", "is", "are", "was", "were", "a", "an",
    "and", "or", "but", "to", "of", "in", "on",
    "for", "with", "by", "at", "from", "as",
    "it", "this", "that", "if", "then",
    "what", "who", "when", "where", "why", "how",
    "does", "do", "did", "can", "could", "would",
    "should", "which", "about", "explain", "tell",
    "me", "please", "happens"
}


CONTRADICTIONS = {
    "labelled": "unlabelled",
    "unlabelled": "labelled",
    "supervised": "unsupervised",
    "unsupervised": "supervised"
}


class ReasoningEngine:

    def __init__(self):
        self.rules = []

    def get_keywords(self, text):

        words = re.findall(
            r'\b[a-zA-Z0-9]+\b',
            text.lower()
        )

        return {
            word for word in words
            if word not in STOPWORDS and len(word) > 1
        }

    def load_rules(self, sentences):

        self.rules = []

        for sentence in sentences:

            match = re.search(
                r'\bif\s+(.+?),?\s+then\s+(.+)',
                sentence,
                re.IGNORECASE
            )

            if match:

                condition = match.group(1).strip()
                conclusion = match.group(2).strip()

                self.rules.append({
                    "condition": condition,
                    "conclusion": conclusion
                })

    def apply_rules(self, question, facts):

        inferred_answers = []

        question_keywords = self.get_keywords(question)

        for rule in self.rules:

            condition_keywords = self.get_keywords(
                rule["condition"]
            )

            if not condition_keywords:
                continue

            # Check for contradictory keywords
            contradiction_found = any(
                CONTRADICTIONS.get(word) in question_keywords
                for word in condition_keywords
                if word in CONTRADICTIONS
            )

            if contradiction_found:
                continue

            # Check whether the question matches the rule
            question_matches = (
                question_keywords & condition_keywords
            )

            question_score = (
                len(question_matches) /
                len(condition_keywords)
            )

            if question_score < 0.70:
                continue

            # Check whether document facts support the condition
            evidence_found = False

            for fact in facts:

                fact_keywords = self.get_keywords(fact)

                evidence_matches = (
                    condition_keywords & fact_keywords
                )

                evidence_score = (
                    len(evidence_matches) /
                    len(condition_keywords)
                )

                if evidence_score >= 0.40:
                    evidence_found = True
                    break

            if evidence_found:

                inferred_answers.append({
                    "conclusion": rule["conclusion"],
                    "condition": rule["condition"],
                    "rule": (
                        "IF " + rule["condition"]
                        + " THEN " + rule["conclusion"]
                    )
                })

        return inferred_answers