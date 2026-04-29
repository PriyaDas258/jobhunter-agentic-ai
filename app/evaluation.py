# app/evaluation.py

import re
from typing import List, Dict


def clean_text(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text.lower())


def keyword_coverage(text: str, required_keywords: List[str]) -> float:
    """
    ATS keyword coverage:
    How many required job keywords appear in the optimized resume?
    """
    text_clean = clean_text(text)

    matched = 0
    for kw in required_keywords:
        if kw.lower() in text_clean:
            matched += 1

    if not required_keywords:
        return 0.0

    return round((matched / len(required_keywords)) * 100, 2)


def resume_job_match_error(expected_score: float, predicted_score: float) -> float:
    """
    Match error:
    Absolute difference between expected human score and app score.
    """
    return round(abs(expected_score - predicted_score), 2)


def skill_gap_accuracy(expected_gaps: List[str], predicted_gaps: List[str]) -> float:
    """
    Skill gap accuracy:
    Measures how many expected missing skills were correctly detected.
    """
    expected = set([x.lower().strip() for x in expected_gaps])
    predicted = set([x.lower().strip() for x in predicted_gaps])

    if not expected:
        return 0.0

    correct = expected.intersection(predicted)
    return round((len(correct) / len(expected)) * 100, 2)


def hallucination_rate(generated_text: str, resume_text: str, allowed_keywords: List[str]) -> float:
    """
    Simple hallucination estimate:
    Checks if generated text mentions skills/tools not present in resume or allowed job keywords.
    """
    common_skills = [
        "python", "java", "sql", "tensorflow", "pytorch", "keras",
        "fastapi", "flask", "django", "docker", "kubernetes",
        "aws", "azure", "gcp", "langchain", "langgraph", "rag",
        "llm", "faiss", "pinecone", "chroma", "postgresql",
        "mongodb", "spark", "databricks", "mlops", "ci/cd",
        "react", "streamlit", "machine learning", "deep learning",
        "nlp", "computer vision", "data science"
    ]

    resume_clean = clean_text(resume_text)
    generated_clean = clean_text(generated_text)
    allowed = set([x.lower() for x in allowed_keywords])

    mentioned_skills = []

    for skill in common_skills:
        if skill in generated_clean:
            mentioned_skills.append(skill)

    hallucinated = []

    for skill in mentioned_skills:
        if skill not in resume_clean and skill not in allowed:
            hallucinated.append(skill)

    if not mentioned_skills:
        return 0.0

    return round((len(hallucinated) / len(mentioned_skills)) * 100, 2)


def human_quality_score(scores: Dict[str, int]) -> float:
    """
    Human quality score:
    Scores should be given from 1 to 5.
    """
    if not scores:
        return 0.0

    total = sum(scores.values())
    max_score = len(scores) * 5

    return round((total / max_score) * 100, 2)


def overall_score(metric_scores: Dict[str, float]) -> float:
    """
    Overall evaluation score.
    For match error, convert error into score: 100 - error.
    """
    if not metric_scores:
        return 0.0

    return round(sum(metric_scores.values()) / len(metric_scores), 2)