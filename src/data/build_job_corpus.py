import pandas as pd

from src.data.load_data import (
    load_linkedin_jobs,
    load_naukri_jobs,
)

from src.data.preprocess import clean_text
from src.config import PROCESSED_DATA


def build_job_corpus():

    linkedin = load_linkedin_jobs()
    naukri = load_naukri_jobs()

    # ---------- LinkedIn ----------
    linkedin = linkedin.rename(columns={
        "title": "Job Title",
        "description": "Description",
        "skills": "Skills"
    })

    # Add missing columns
    linkedin["Company"] = "Unknown"
    linkedin["Location"] = "Unknown"
    linkedin["Experience"] = ""
    linkedin["Salary"] = ""

    # ---------- Naukri ----------
    naukri = naukri.rename(columns={
        "title": "Job Title",
        "company": "Company",
        "location": "Location",
        "job-description": "Description",
        "skills": "Skills",
        "experience": "Experience",
        "salary": "Salary"
    })

    required_columns = [
        "Job Title",
        "Company",
        "Location",
        "Description",
        "Skills",
        "Experience",
        "Salary"
    ]

    # Ensure all required columns exist
    for col in required_columns:
        if col not in linkedin.columns:
            linkedin[col] = ""

        if col not in naukri.columns:
            naukri[col] = ""

    linkedin = linkedin[required_columns]
    naukri = naukri[required_columns]

    jobs = pd.concat([linkedin, naukri], ignore_index=True)

    jobs = jobs.fillna("")

    jobs["combined_text"] = (
        jobs["Job Title"] + " " +
        jobs["Description"] + " " +
        jobs["Skills"]
    )

    jobs["clean_text"] = jobs["combined_text"].apply(clean_text)

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

    jobs.to_csv(
        PROCESSED_DATA / "job_corpus.csv",
        index=False,
    )

    print("\nJob Corpus Created Successfully!")
    print(jobs.head())
    print("\nShape:", jobs.shape)


if __name__ == "__main__":
    build_job_corpus()