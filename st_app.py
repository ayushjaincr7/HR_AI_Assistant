

import streamlit as st
from app.services.screening_service import screen_resume
from app.utils.pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="HR AI Assistant", layout="wide")

st.title("🤖 HR AI Resume Screening Assistant")

# Upload PDF
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# Fallback text input
resume_text_input = st.text_area("Or paste resume text", height=200)

job_description = st.text_area("💼 Job Description", height=300)

resume_text = ""

# Extract text
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF uploaded and text extracted!")

elif resume_text_input:
    resume_text = resume_text_input

if st.button("🚀 Screen Candidate"):
    if resume_text and job_description:
        with st.spinner("Analyzing resume..."):
            result = screen_resume(resume_text, job_description)

        st.subheader("📊 Result")
        st.write(result)
    else:
        st.warning("Please upload a resume or paste text + job description")