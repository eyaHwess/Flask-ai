import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), "../spam classifier/spam_classifier.joblib")
model = joblib.load(model_path)
# i added the test on an empty stirng first if its empty it returns ham with a score of 0.0
def detect_spam(text, threshold=0.56):
    if not text.strip():
        return { "label": "ham", "score": 0.0 }
    prob = model.predict_proba([text])[0][1]
    return {
        "label": "spam" if prob > threshold else "ham",
        "score": prob
    }
