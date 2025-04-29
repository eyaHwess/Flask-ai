from better_profanity import profanity

profanity.load_censor_words()

def has_profanity(text):
    return profanity.contains_profanity(text)
