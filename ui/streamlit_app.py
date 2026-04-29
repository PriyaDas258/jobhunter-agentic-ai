from pypdf import PdfReader
from io import BytesIO
import streamlit as st
import requests

st.set_page_config(
    page_title="JobHunter Agentic AI",
    page_icon="🤖",
    layout="wide"
)

# -------- PDF TEXT EXTRACTOR --------
def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# -------- STYLING --------
st.markdown("""
<style>
.main {background-color: #f7f9fc;}
.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #1f2937, #2563eb);
    color: white;
    margin-bottom: 2rem;
}
.card {
    padding: 1.5rem;
    border-radius: 18px;
    background-color: white;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}
.score {
    font-size: 42px;
    font-weight: 800;
    color: #2563eb;
}
</style>
""", unsafe_allow_html=True)

# -------- HERO --------
st.markdown("""
<div class="hero">
    <h1>🤖 JobHunter Agentic AI</h1>
    <p>Upload your resume or paste it. AI agents will optimize everything.</p>
</div>
""", unsafe_allow_html=True)

# -------- INPUT SECTION --------
left, right = st.columns(2)

with left:
    st.markdown("### 📄 Resume Input")

    upload_option = st.radio(
        "Choose input method:",
        ["Upload PDF", "Paste Text"]
    )

    resume_text = ""

    if upload_option == "Upload PDF":
        uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

        if uploaded_file:
            resume_text = extract_text_from_pdf(uploaded_file)
            st.success("Resume uploaded and extracted ✅")
            st.text_area("Extracted Resume Preview", resume_text, height=200)

    else:
        resume_text = st.text_area(
            "Paste your resume",
            height=300
        )

with right:
    st.markdown("### 💼 Job Description")

    job = st.text_area(
        "Paste job description here",
        height=320
    )

# -------- RUN BUTTON --------
st.markdown("---")
run_button = st.button("🚀 Run Agentic AI Analysis", use_container_width=True)

# -------- RESULT --------
if run_button:
    if not resume_text.strip() or not job.strip():
        st.warning("Please provide resume and job description.")
    else:
        with st.spinner("Agents are working..."):
            response = requests.post(
                "http://localhost:8000/analyze-job",
                json={
                    "resume_text": resume_text,
                    "job_description": job
                }
            )

        if response.status_code == 200:
            result = response.json()

            st.success("Analysis complete!")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown("### 🎯 Match Score")
                st.markdown(
                    f'<div class="score">{result["match_score"]}%</div>',
                    unsafe_allow_html=True
                )
                st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown("### ⚠️ Skill Gaps")
                for gap in result["skill_gaps"]:
                    st.write(f"• {gap}")
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("## ✨ Outputs")

            tab1, tab2, tab3 = st.tabs(
                ["📄 Resume", "✉️ Cover Letter", "🤝 LinkedIn"]
            )

            with tab1:
                st.write(result["optimized_resume"])

            with tab2:
                st.write(result["cover_letter"])

            with tab3:
                st.write(result["linkedin_message"])

        else:
            st.error("Backend error. Check FastAPI.")