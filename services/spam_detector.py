import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), "../spam classifier/spam_classifier.joblib")
model = joblib.load(model_path)

def detect_spam(text, threshold=0.56):
    prob = model.predict_proba([text])[0][1]  # probability it's spam
    return {
        "label": "spam" if prob > threshold else "ham",
        "score": prob
    }
