from src.features.skill_extractor import extract_skills


def skill_gap(resume_text,job_text):

    resume_skills=set(
        extract_skills(resume_text)
    )

    job_skills=set(
        extract_skills(job_text)
    )

    missing=job_skills-resume_skills

    matched=resume_skills & job_skills

    score=0

    if len(job_skills)>0:

        score=len(matched)/len(job_skills)*100

    return{

        "Resume Skills":sorted(resume_skills),

        "Matched Skills":sorted(matched),

        "Missing Skills":sorted(missing),

        "Resume Score":round(score,2)

    }