# tests/test_evaluation.py

from app.evaluation import (
    keyword_coverage,
    resume_job_match_error,
    skill_gap_accuracy,
    hallucination_rate,
    human_quality_score,
    overall_score
)

resume_text = """
Priya Das has experience in Python, Machine Learning, Deep Learning,
RAG, LangChain, FastAPI, TensorFlow, PyTorch, SQL, and Streamlit.
"""

job_description = """
We are hiring an AI Engineer with experience in Python, RAG,
LangGraph, FastAPI, Docker, Kubernetes, vector databases, and MLOps.
"""

optimized_resume = """
AI Engineer with experience in Python, RAG, LangChain, LangGraph,
FastAPI, Docker, MLOps, TensorFlow, PyTorch, and Streamlit.
"""

generated_cover_letter = """
Dear Hiring Manager,

I am excited to apply for the AI Engineer role. My background includes
Python, Machine Learning, RAG systems, LangChain, FastAPI, and Streamlit.
I am also interested in applying LangGraph and Docker for production AI systems.

Best regards,
Priya Das
"""

generated_email = """
Subject: Application for AI Engineer Role

Dear Hiring Manager,

Please find my application for the AI Engineer role. My experience includes
Python, RAG, FastAPI, Machine Learning, and Deep Learning.

Best regards,
Priya Das
"""

required_keywords = [
    "Python", "RAG", "LangGraph", "FastAPI",
    "Docker", "Kubernetes", "MLOps"
]

expected_skill_gaps = [
    "LangGraph", "Docker", "Kubernetes", "MLOps"
]

predicted_skill_gaps = [
    "Docker", "LangGraph", "Production Deployment"
]

allowed_keywords = required_keywords

expected_match_score = 85.0
predicted_match_score = 78.5


match_error = resume_job_match_error(expected_match_score, predicted_match_score)

skill_accuracy = skill_gap_accuracy(
    expected_skill_gaps,
    predicted_skill_gaps
)

ats_coverage = keyword_coverage(
    optimized_resume,
    required_keywords
)

cover_letter_hallucination = hallucination_rate(
    generated_cover_letter,
    resume_text,
    allowed_keywords
)

email_hallucination = hallucination_rate(
    generated_email,
    resume_text,
    allowed_keywords
)

cover_letter_quality = human_quality_score({
    "personalized_to_job": 4,
    "professional_tone": 5,
    "mentions_relevant_skills": 4,
    "no_hallucination": 4,
    "grammar": 5
})

email_quality = human_quality_score({
    "clear_subject": 5,
    "professional_tone": 5,
    "concise": 4,
    "mentions_role": 5,
    "grammar": 5
})

match_score_accuracy = 100 - match_error

final_score = overall_score({
    "match_score_accuracy": match_score_accuracy,
    "skill_gap_accuracy": skill_accuracy,
    "ats_keyword_coverage": ats_coverage,
    "cover_letter_quality": cover_letter_quality,
    "email_quality": email_quality,
    "cover_letter_non_hallucination": 100 - cover_letter_hallucination,
    "email_non_hallucination": 100 - email_hallucination
})

print("\n===== JobHunter Agentic AI Evaluation =====")
print(f"Resume-Job Match Error: {match_error}%")
print(f"Match Score Accuracy: {match_score_accuracy}%")
print(f"Skill-Gap Detection Accuracy: {skill_accuracy}%")
print(f"ATS Keyword Coverage: {ats_coverage}%")
print(f"Cover Letter Hallucination Rate: {cover_letter_hallucination}%")
print(f"Email Hallucination Rate: {email_hallucination}%")
print(f"Cover Letter Human Quality Score: {cover_letter_quality}%")
print(f"HR Email Human Quality Score: {email_quality}%")
print(f"Overall Evaluation Score: {final_score}%")