import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data-reviews-utf8.csv")

#(ham = 0, spam = 1)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

#Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['label'], test_size=0.2, random_state=42)

#Create pipeline with class weight balancing
#it should treat the data equeally even if there is more spam than ham or the opposite
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(class_weight='balanced'))
])

#Train the model
pipeline.fit(X_train, y_train)

#Evaluate it
y_pred = pipeline.predict(X_test)
print("\n Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=["ham", "spam"]))

#Save
joblib.dump(pipeline, "spam_classifier.joblib")
print("\n Model saved as spam_classifier.joblib")
