import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("fitness_data.csv")

X = data["question"]
y = data["answer"]

# Convert text to vectors
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model
with open("fitness_bot.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Model trained and saved as fitness_bot.pkl")
