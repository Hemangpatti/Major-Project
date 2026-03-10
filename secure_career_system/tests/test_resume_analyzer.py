from secure_career_system.resume_analyzer import analyze_resume


def test_analyze_nonexistent_pdf():
    # If file doesn't exist analyzer should return empty or minimal structure
    res = analyze_resume('nonexistent.pdf')
    assert 'found_skills' in res
    assert 'skill_gaps' in res
