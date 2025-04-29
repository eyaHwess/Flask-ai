def detect_spam(text):
    words = text.lower().split()

    is_spam = False

    # Rule 1: Very short review (≤3 words)
    if len(words) <= 3:
        is_spam = True

    # Rule 2: Excessive exclamation marks
    if text.count('!') >= 3:
        is_spam = True

    # Rule 3: Highly repetitive words
    if len(set(words)) < len(words) / 2:
        is_spam = True

    return {
        "label": "SPAM" if is_spam else "HAM",
        "score": 1.0 if is_spam else 0.0 
    }
