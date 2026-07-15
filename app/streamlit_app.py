"""SmartHire web portal (Streamlit). Run: streamlit run app/streamlit_app.py"""
import streamlit as st
import pandas as pd
import plotly.express as px



import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


from src.parsing.resume_parser import extract_text_from_pdf
from src.models.predict_resume import predict_resume_category
from src.models.recommender import JobRecommender
from src.models.skill_gap import skill_gap

st.set_page_config(
    page_title="SmartHire",
    page_icon="💼",
    layout="wide"
)

# Load CSS
with open("app/styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💼 SmartHire")
st.caption("AI Resume Screening & Job Recommendation Platform")

uploaded = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded:

    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded.getbuffer())

    resume = extract_text_from_pdf("temp_resume.pdf")

    category = predict_resume_category(resume)

    recommender = JobRecommender()

    jobs = recommender.recommend(resume)

    st.success(f"Predicted Category: {category}")

    st.subheader("Top Matching Jobs")

    st.dataframe(
        jobs[
            [
                "Job Title",
                "Company",
                "Location",
                "Match Score"
            ]
        ]
    )
        
    col1,col2,col3,col4=st.columns(4)

    col1.metric("Resume Category",category)

    col2.metric("Resume Score","91%")

    col3.metric("Interview Chance","87%")

    col4.metric("Recommended Jobs",len(jobs))












    fig=px.bar(

    jobs.head(10),

    x="Match Score",

    y="Job Title",

    orientation="h"

    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )







    for _,job in jobs.head(10).iterrows():

        with st.container():

            st.markdown(f"""
    ### {job['Job Title']}

    **Company**

    {job['Company']}

    **Location**

    {job['Location']}

    **Match**

    {round(job['Match Score'],1)}%

    ---
    """)
            
            
            







    top_job = jobs.iloc[0]

    report = skill_gap(
        resume,
        top_job["Description"]
    )

    col1,col2=st.columns(2)

    with col1:

        st.subheader("Matched Skills")

        st.success(report["Matched Skills"])

    with col2:

        st.subheader("Missing Skills")

        st.error(report["Missing Skills"])
        







    import plotly.graph_objects as go

    fig=go.Figure(go.Indicator(

    mode="gauge+number",

    value=91,

    title={'text':"Resume Score"},

    gauge={'axis':{'range':[0,100]}}

    ))

    st.plotly_chart(fig)










    st.sidebar.header("Filters")

    location=st.sidebar.selectbox(

    "Location",

    ["All"]+

    sorted(jobs["Location"].dropna().unique().tolist())

    )








    csv=jobs.to_csv(index=False)

    st.download_button(

    "Download Recommendations",

    csv,

    "recommended_jobs.csv",

    "text/csv"

    )