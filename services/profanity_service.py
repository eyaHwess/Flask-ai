from better_profanity import profanity

profanity.load_censor_words()

def has_profanity(text):
    result = profanity.contains_profanity(text)
    print(f"[ProfanityCheck] Text: '{text}' | Contains Profanity? {result}")
    return result