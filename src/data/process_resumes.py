from src.data.load_data import load_resume_data
from src.data.preprocess import clean_text

from src.config import PROCESSED_DATA


def process_resumes():

    resumes = load_resume_data()

    print(resumes.columns)

    # Change these names if your dataset differs.
    resumes["clean_resume"] = resumes["Resume"].apply(clean_text)

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

    resumes.to_csv(
        PROCESSED_DATA / "processed_resumes.csv",
        index=False,
    )

    print(resumes.head())


if __name__ == "__main__":
    process_resumes()