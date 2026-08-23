"""
Resume-to-Job-Fit Analyzer
----------------------------
Scores how well a resume matches a job description using keyword/skill
overlap, and returns an explainable breakdown (matched skills, missing
skills, overall fit score).

Run:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel
from app.matcher import analyze_fit

app = FastAPI(
    title="Resume-to-Job-Fit Analyzer",
    description="Explainable resume vs job description matching.",
    version="0.1.0",
)


class FitRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def root():
    return {"status": "ok", "service": "resume-job-fit-analyzer"}


@app.post("/analyze")
def analyze(req: FitRequest):
    return analyze_fit(req.resume_text, req.job_description)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
