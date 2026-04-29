# JobHunter Agentic AI

An end-to-end Agentic AI system that automates the job application process using multi-agent orchestration.
It analyzes job descriptions, optimizes resumes, generates cover letters, creates recruiter outreach messages, and exports everything as a downloadable PDF.

---

## Features

- Resume Upload (PDF/Text)
- Resume–Job Matching Score
- Skill Gap Detection
- ATS-Optimized Resume Generation
- Personalized Cover Letter Generation
- LinkedIn Networking Message Generator
- Professional HR Email Generator
- Download Full Application as PDF
- Multi-Agent Workflow using LangGraph

---

## System Architecture

The system uses a multi-agent pipeline:

Resume → Match Agent → Resume Optimizer → Cover Letter Agent
→ Networking Agent → Email Agent → Final Output


Each component is implemented as an independent agent coordinated using a graph-based workflow.

---

## Tech Stack

- Backend: FastAPI
- Frontend: Streamlit
- Agent Framework: LangGraph
- Vector Search: FAISS / Pinecone
- PDF Processing: pypdf
- PDF Generation: reportlab
- Deployment: Docker + Render + Streamlit Cloud

---

## Project Structure


jobhunter-agentic-ai/
│
├── app/
│   ├── main.py
│   ├── graph.py
│   ├── evaluation.py
│
├── ui/
│   └── streamlit_app.py
│
├── tests/
│   └── test_evaluation.py
│
├── requirements.txt
├── Dockerfile
└── README.md


---

## Installation

### 1. Clone repository

git clone https://github.com/YOUR_USERNAME/jobhunter-agentic-ai.git
cd jobhunter-agentic-ai


### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


---

## Run Locally

### Start backend (FastAPI)

uvicorn app.main:app --reload


Visit:

http://127.0.0.1:8000/docs


---

### Start frontend (Streamlit)

streamlit run ui/streamlit_app.py


---

## Evaluation Metrics

This project evaluates performance using **component-level metrics**:

| Metric                 | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| Resume–Job Match Error | Difference between expected and predicted match score |
| Skill Gap Accuracy     | Correctly identified missing skills                   |
| ATS Keyword Coverage   | % of job keywords present in optimized resume         |
| Hallucination Rate     | % of unsupported skills generated                     |
| Human Quality Score    | Manual scoring for cover letter & email               |

### Run evaluation

python3 -m tests.test_evaluation


---

## Sample Output

Match Score: 78.5%
Skill Gaps: Docker, LangGraph
Cover Letter: Generated
Email: Generated
Overall Evaluation Score: ~85%

---

## Deployment

### Backend (Render)

1. Push code to GitHub
2. Create Web Service on Render
3. Select Docker deployment
4. Deploy

---

### Frontend (Streamlit Cloud)

1. Connect GitHub repo
2. Select:
ui/streamlit_app.py

3. Deploy

---

## Use Case

This project simulates a real-world AI assistant for job seekers:

* Automates job applications
* Improves ATS compatibility
* Generates recruiter-ready communication
* Reduces manual effort

---

## Key Highlights

* Multi-agent architecture using LangGraph
* End-to-end automation pipeline
* Real-world applicability (job search automation)
* Production-ready structure (API + UI + deployment)

---

## 📌 Author

**Priya Das**
Machine Learning | GenAI | Agentic AI

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
