import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


# Load datasets
news = pd.read_csv("dataset/news.csv")
custom = pd.read_csv(
    "dataset/custom_news.csv",
    skip_blank_lines=True
)

fake = pd.read_csv("dataset/Fake.csv")
true = pd.read_csv("dataset/True.csv")


# Add labels
fake["label"] = 0
true["label"] = 1


# Combine datasets
data = pd.concat(
    [news, custom, fake, true],
    ignore_index=True
)


# Remove empty rows
data = data.dropna()


# Shuffle data
data = data.sample(frac=1, random_state=42).reset_index(drop=True)


# Fix label datatype
data["label"] = pd.to_numeric(data["label"], errors="coerce")
data = data.dropna(subset=["label"])

data["label"] = data["label"].astype(int)


print("Dataset size:", data.shape)
print(data["label"].value_counts())


# Features and target
X = data["text"].astype(str)
y = data["label"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(stop_words="english")
    ),
    (
        "classifier",
        LogisticRegression(max_iter=1000)
    )
])


# Train
model.fit(X_train, y_train)


# Accuracy
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)


# Save model
joblib.dump(model, "fake_news_model.pkl")


print("Model saved successfully!")