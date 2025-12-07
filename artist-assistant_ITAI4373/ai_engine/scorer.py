import re

def score_opportunity(text: str) -> float:
    text = text.lower()

    strong_signals = [
        r"looking for an artist",
        r"commission",
        r"need.*art",
        r"paying",
        r"hiring.*artist",
        r"portrait commission"
    ]

    medium_signals = [
        r"digital art",
        r"portrait",
        r"art style",
        r"illustration"
    ]

    score = 0

    for s in strong_signals:
        if re.search(s, text):
            score += 0.6

    for s in medium_signals:
        if re.search(s, text):
            score += 0.3

    return min(score, 1.0)
