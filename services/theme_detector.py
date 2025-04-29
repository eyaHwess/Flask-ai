from sentence_transformers import SentenceTransformer
from keybert import KeyBERT

embedder = SentenceTransformer('all-MiniLM-L6-v2')
kw_model = KeyBERT(model=embedder)

def detect_themes(reviews):
    if not reviews:
        return []
    joined_text = " ".join(reviews)

    keywords = kw_model.extract_keywords(
        joined_text,
        keyphrase_ngram_range=(1, 3),
        stop_words='english',
        top_n=5
    )
    theme_keywords = [kw for kw, _ in keywords]
    return theme_keywords