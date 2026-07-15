from src.models.recommender import JobRecommender

resume = """
Python
Machine Learning
SQL
Pandas
NumPy
TensorFlow
Power BI
Data Analysis
AWS
"""

engine = JobRecommender()

jobs = engine.recommend(resume)

print(
    jobs[
        [
            "Job Title",
            "Company",
            "Location",
            "Match Score",
        ]
    ]
)