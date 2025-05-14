import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Step 1: Load the labeled UTF-8 CSV
df = pd.read_csv("data-reviews-utf8.csv")

# Step 2: Encode labels (ham = 0, spam = 1)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Step 3: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['label'], test_size=0.2, random_state=42)

# Step 4: Create pipeline with class weight balancing
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(class_weight='balanced'))
])

# Step 5: Train the model
pipeline.fit(X_train, y_train)

# Step 6: Evaluate it
y_pred = pipeline.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=["ham", "spam"]))

# Step 7: Save the trained model
joblib.dump(pipeline, "spam_classifier.joblib")
print("\n✅ Model saved as spam_classifier.joblib")
