import joblib
from src.config import MODEL_PATH


model = joblib.load(
    MODEL_PATH / "classifier.pkl"
)


def predict_resume_category(resume_text):

    prediction = model.predict([resume_text])

    return prediction[0]


if __name__ == "__main__":

    sample = """
    Python
    Machine Learning
    SQL
    Data Analysis
    Pandas
    NumPy
    Power BI
    """

    print(predict_resume_category(sample))