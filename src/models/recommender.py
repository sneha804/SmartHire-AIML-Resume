"""Unsupervised content-based recommender: cosine-similarity job ranking (top-N)."""
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.config import PROCESSED_DATA, MODEL_PATH


class JobRecommender:

    def __init__(self):

        self.jobs = pd.read_csv(
            PROCESSED_DATA / "job_corpus.csv"
        )

        self.vectorizer = TfidfVectorizer(
            max_features=10000,
            stop_words="english",
            ngram_range=(1,2)
        )

        self.job_vectors = self.vectorizer.fit_transform(
            self.jobs["clean_text"]
        )

    def save(self):

        MODEL_PATH.mkdir(exist_ok=True)

        joblib.dump(
            self.vectorizer,
            MODEL_PATH / "job_vectorizer.pkl"
        )

        joblib.dump(
            self.job_vectors,
            MODEL_PATH / "job_vectors.pkl"
        )

    def recommend(self,resume_text,top_n=10):

        resume_vector = self.vectorizer.transform(
            [resume_text]
        )

        similarity = cosine_similarity(
            resume_vector,
            self.job_vectors
        )

        self.jobs["Match Score"] = similarity.flatten()*100

        results = self.jobs.sort_values(
            by="Match Score",
            ascending=False
        )

        return results.head(top_n)


if __name__=="__main__":

    recommender=JobRecommender()

    recommender.save()

    print("Recommendation model saved.")