from app.matcher import analyze_fit


def test_analyze_fit_basic():
    resume = "Experienced Python developer with FastAPI, Docker, and AWS background."
    jd = "Looking for a Python developer skilled in FastAPI, Docker, Kubernetes, and AWS."
    result = analyze_fit(resume, jd)
    assert "python" in result["matched_skills"]
    assert "kubernetes" in result["missing_skills"]
    assert 0 < result["fit_score"] <= 1


def test_analyze_fit_no_overlap():
    result = analyze_fit("I like painting and gardening.", "Looking for a React developer.")
    assert result["matched_skills"] == []
    assert result["fit_score"] == 0.0
