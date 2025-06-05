# app.py

import streamlit as st
import os
import requests
from io import BytesIO
from docx import Document
from PyPDF2 import PdfReader


# Load API keys from environment variables
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

st.set_page_config(page_title="NeuroMind AI - Smarter Job Search", layout="wide")

st.title("🧠 NeuroMind AI – Smarter Job Search")

st.markdown("""
Upload your resume (PDF/DOCX) or enter a job query to get AI-powered job suggestions, salary info, and interview prep resources.
""")

# --- Helper Functions ---

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)

def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file format! Please upload PDF or DOCX.")
        return ""

def query_huggingface_resume_analyzer(text):
    # Example: Using a zero-shot-classification model to suggest job titles
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    candidate_labels = ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer", "DevOps Engineer", "Marketing Manager", "Sales", "Business Analyst"]
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": candidate_labels},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        labels = result.get("labels", [])
        scores = result.get("scores", [])
        top_matches = labels[:3]
        return top_matches
    else:
        st.error("Error querying Hugging Face API")
        return []

def query_serpapi_jobs(query):
    SERPAPI_URL = "https://serpapi.com/search.json"
    params = {
        "engine": "duckduckgo_jobs",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "hl": "en",
        "gl": "us",
        "num": 10
    }
    response = requests.get(SERPAPI_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        jobs = data.get("jobs_results", [])
        return jobs
    else:
        st.error("Error fetching jobs from SerpAPI")
        return []

def build_salary_link(job_title):
    # Levels.fyi URL example for tech jobs
    base_url = "https://www.levels.fyi/search/?searchTerm="
    return base_url + job_title.replace(" ", "+")

def build_interview_link(company_name):
    base_url = "https://www.glassdoor.com/Interview/"
    company_slug = company_name.replace(" ", "-")
    return f"{base_url}{company_slug}-Interview-EI_IE.htm"

# --- Streamlit UI ---

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
query_text = st.text_input("Or enter a job title or keywords:")

if st.button("Analyze & Search Jobs"):
    if uploaded_file:
        raw_text = extract_text(uploaded_file)
        if raw_text:
            st.subheader("Extracted Resume Text Preview")
            st.text_area("", raw_text[:1000], height=200)
            job_titles = query_huggingface_resume_analyzer(raw_text)
            if job_titles:
                st.success(f"Suggested job titles: {', '.join(job_titles)}")
                selected_title = st.selectbox("Select a job title to search", job_titles)
                jobs = query_serpapi_jobs(selected_title)
            else:
                st.warning("Could not suggest job titles, try entering a query manually.")
                jobs = []
        else:
            jobs = []
    elif query_text:
        jobs = query_serpapi_jobs(query_text)
    else:
        st.warning("Please upload a resume or enter a job query.")
        jobs = []

    if jobs:
        st.subheader("Job Results")
        for job in jobs:
            title = job.get("title")
            company = job.get("company_name")
            location = job.get("location")
            link = job.get("link")
            st.markdown(f"### [{title}]({link})")
            st.markdown(f"**Company:** {company} | **Location:** {location}")
            st.markdown(f"[Salary Info on Levels.fyi]({build_salary_link(title)}) | [Interview Prep on Glassdoor]({build_interview_link(company)})")
            st.markdown("---")
    else:
        st.info("No jobs found or no search performed yet.")
