"""
Explainable resume-vs-job-description matcher.

Approach: extract a candidate skill/keyword set from both texts using a
curated skill vocabulary + simple noun-phrase heuristics, then compute
overlap. This keeps the project dependency-free and fully explainable
(no black-box embedding model) — a good property to highlight in a demo.

For higher recall on real-world resumes, swap `SKILL_VOCAB` for a larger
list (e.g. from ESCO or O*NET) or add a sentence-embedding similarity
layer on top.
"""

import re

SKILL_VOCAB = [
    "python", "java", "javascript", "typescript", "c++", "c#", "sql", "nosql",
    "react", "angular", "vue", "node.js", "django", "flask", "fastapi",
    "aws", "azure", "gcp", "docker", "kubernetes", "ci/cd", "git",
    "machine learning", "deep learning", "nlp", "computer vision",
    "data analysis", "pandas", "numpy", "tensorflow", "pytorch",
    "rest api", "graphql", "microservices", "agile", "scrum",
    "html", "css", "figma", "ui/ux", "project management",
    "communication", "leadership", "problem solving",
]


def _extract_skills(text: str) -> set:
    lower = text.lower()
    return {skill for skill in SKILL_VOCAB if skill in lower}


def analyze_fit(resume_text: str, job_description: str) -> dict:
    resume_skills = _extract_skills(resume_text)
    jd_skills = _extract_skills(job_description)

    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)

    fit_score = round(len(matched) / len(jd_skills), 2) if jd_skills else 0.0

    return {
        "fit_score": fit_score,
        "matched_skills": matched,
        "missing_skills": missing,
        "total_required_skills": len(jd_skills),
    }
