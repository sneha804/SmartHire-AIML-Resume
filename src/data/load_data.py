"""Read raw datasets from data/raw/ (load_resumes, load_jobs)."""
import pandas as pd
from src.config import RAW_DATA


def load_resume_data():
    return pd.read_csv(RAW_DATA / "Resume_25.csv")


def load_linkedin_jobs():
    return pd.read_csv(RAW_DATA / "Linkedin_dataset.csv")


def load_naukri_jobs():
    return pd.read_csv(RAW_DATA / "naukri.csv")