from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import jobhunter_graph

app = FastAPI(title="JobHunter Agentic AI")

class JobRequest(BaseModel):
    resume_text: str
    job_description: str

@app.get("/")
def home():
    return {"message": "JobHunter Agentic AI backend is running"}

@app.post("/analyze-job")
def analyze_job(request: JobRequest):
    result = jobhunter_graph.invoke({
        "resume_text": request.resume_text,
        "job_description": request.job_description,
        "match_score": 0.0,
        "skill_gaps": [],
        "optimized_resume": "",
        "cover_letter": "",
        "linkedin_message": "",
        "email_text": ""
    })
    return result