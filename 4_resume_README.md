# 📋 Resume-to-Job-Fit Analyzer

Explainable resume-vs-job-description matcher — see exactly which skills
match, which are missing, and an overall fit score. No black-box model,
fully transparent scoring.

## Quickstart

```bash
git clone https://github.com/<your-username>/resume-job-fit-analyzer.git
cd resume-job-fit-analyzer
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example

```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Experienced Python developer with FastAPI, Docker, and AWS background.",
    "job_description": "Looking for a Python developer skilled in FastAPI, Docker, Kubernetes, and AWS."
  }'
```

Returns:
```json
{
  "fit_score": 0.75,
  "matched_skills": ["aws", "docker", "fastapi", "python"],
  "missing_skills": ["kubernetes"],
  "total_required_skills": 4
}
```

## Project structure

```
resume-job-fit-analyzer/
├── app/
│   ├── main.py      # FastAPI routes
│   └── matcher.py   # Skill extraction + fit scoring
├── tests/
└── requirements.txt
```

## Roadmap

- [ ] Expand `SKILL_VOCAB` with an ESCO/O*NET-based taxonomy
- [ ] Add PDF resume upload support
- [ ] Add sentence-embedding similarity for soft-skill matching

## Tests

```bash
pytest tests/
```

## License

MIT
