import pytest
from src.classifier import JobClassifier

@pytest.fixture
def classifier():
    return JobClassifier()

def test_classify_returns_dict(classifier):
    result = classifier.classify("Python machine learning data scientist NLP")
    assert isinstance(result, dict)

def test_classify_has_category(classifier):
    result = classifier.classify("Python machine learning data scientist")
    assert "category" in result

def test_classify_has_confidence(classifier):
    result = classifier.classify("DevOps kubernetes docker ci/cd")
    assert "confidence" in result
    assert 0 <= result["confidence"] <= 1

def test_classify_all_scores(classifier):
    result = classifier.classify("Product manager roadmap agile scrum")
    assert "all_scores" in result
    assert len(result["all_scores"]) > 0