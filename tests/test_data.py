from src.data.load_data import (
    load_resume_data,
    load_linkedin_jobs,
    load_naukri_jobs,
)

resume = load_resume_data()
linkedin = load_linkedin_jobs()
naukri = load_naukri_jobs()

print(resume.head())
print(linkedin.head())
print(naukri.head())

print(resume.shape)
print(linkedin.shape)
print(naukri.shape)