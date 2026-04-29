from typing import TypedDict
from langgraph.graph import StateGraph, END

# -------- STATE --------
class JobHunterState(TypedDict):
    resume_text: str
    job_description: str
    match_score: float
    skill_gaps: list
    optimized_resume: str
    cover_letter: str
    linkedin_message: str
    email_text: str


# -------- AGENTS --------

def match_job(state: JobHunterState):
    # Dummy logic (later replace with embeddings)
    return {
        "match_score": 78.5,
        "skill_gaps": ["Docker", "LangGraph", "Production Deployment"]
    }


def optimize_resume(state: JobHunterState):
    return {
        "optimized_resume": f"""
Optimized Resume:

Based on the job description, emphasize:
- Machine Learning
- GenAI / RAG
- FastAPI
- Deployment skills

Original Resume:
{state['resume_text'][:500]}
"""
    }


def generate_cover_letter(state: JobHunterState):
    return {
        "cover_letter": f"""
Dear Hiring Manager,

I am excited to apply for this role.

With experience in Machine Learning, RAG systems, and AI pipelines,
I believe I am a strong fit for this position.

Looking forward to contributing to your team.

Best regards,
Priya Das
"""
    }


def generate_networking_message(state: JobHunterState):
    return {
        "linkedin_message": f"""
Hi, I’m Priya. I work in ML/AI and recently moved to Canada.
I came across your profile and would love to connect.
"""
    }


def generate_email(state: JobHunterState):
    return {
        "email_text": f"""
Subject: Application for AI Role

Dear Hiring Manager,

I hope you are doing well.

I am writing to express my interest in this role.
Please find my resume attached.

Looking forward to hearing from you.

Best regards,
Priya Das
"""
    }


# -------- GRAPH --------

graph = StateGraph(JobHunterState)

graph.add_node("match_job", match_job)
graph.add_node("optimize_resume", optimize_resume)
graph.add_node("generate_cover_letter", generate_cover_letter)
graph.add_node("generate_networking_message", generate_networking_message)
graph.add_node("generate_email", generate_email)

graph.set_entry_point("match_job")

graph.add_edge("match_job", "optimize_resume")
graph.add_edge("optimize_resume", "generate_cover_letter")
graph.add_edge("generate_cover_letter", "generate_networking_message")
graph.add_edge("generate_networking_message", "generate_email")
graph.add_edge("generate_email", END)

jobhunter_graph = graph.compile()