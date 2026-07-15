"""Supervised resume category classifier (train / predict / save / load)."""
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

from src.config import PROCESSED_DATA, MODEL_PATH


def train_classifier():

    # Load data
    data = pd.read_csv(PROCESSED_DATA / "processed_resumes.csv")

    print("Columns:", data.columns.tolist())

    # Clean dataset
    data = data.drop_duplicates()
    data = data.dropna(subset=["clean_resume", "Category"])
    data["clean_resume"] = data["clean_resume"].fillna("").astype(str)
    data = data[data["clean_resume"].str.strip() != ""]

    print("Dataset Shape:", data.shape)

    X = data["clean_resume"]
    y = data["Category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000)),
        ("svm", LinearSVC())
    ])

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report\n")
    print(classification_report(y_test, predictions))

    MODEL_PATH.mkdir(exist_ok=True)

    joblib.dump(model, MODEL_PATH / "classifier.pkl")

    print("\nModel saved successfully.")


if __name__ == "__main__":
    train_classifier()