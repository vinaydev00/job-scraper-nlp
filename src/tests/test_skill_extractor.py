from src.skill_extractor import SkillExtractor

def test_extract_finds_python():
    e = SkillExtractor()
    result = e.extract("We need a Python developer with SQL experience.")
    names = [s.name for s in result]
    assert "Python" in names

def test_extract_frequency():
    e = SkillExtractor()
    result = e.extract("Python Python Python SQL")
    python_skill = next((s for s in result if s.name == "Python"), None)
    assert python_skill is not None
    assert python_skill.frequency == 3

def test_get_categories():
    e = SkillExtractor()
    result = e.get_categories("Python Docker AWS Kubernetes")
    assert "devops" in result or "cloud" in result

def test_empty_text():
    e = SkillExtractor()
    result = e.extract("")
    assert result == []