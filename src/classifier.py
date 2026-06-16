"""
NLP Job Classifier - Classifies job listings into categories
using TF-IDF + Logistic Regression.
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

JOB_CATEGORIES = [
    "Data Science", "Software Engineering", "DevOps",
    "Product Management", "Design", "Marketing", "HR"
]

CATEGORY_KEYWORDS = {
    "Data Science": ["machine learning", "data scientist", "nlp", "deep learning", "python", "tensorflow"],
    "Software Engineering": ["software engineer", "backend", "frontend", "full stack", "api", "java", "react"],
    "DevOps": ["devops", "kubernetes", "docker", "ci/cd", "infrastructure", "terraform", "aws"],
    "Product Management": ["product manager", "roadmap", "stakeholders", "go-to-market", "agile", "scrum"],
    "Design": ["ui/ux", "figma", "design", "wireframe", "prototype", "user research"],
    "Marketing": ["marketing", "seo", "content", "social media", "campaigns", "growth"],
    "HR": ["recruiter", "talent acquisition", "onboarding", "hr", "people ops", "payroll"],
}

class JobClassifier:
    def __init__(self):
        self.pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
            ("clf", LogisticRegression(max_iter=1000)),
        ])
        self.trained = False
        self._train_on_synthetic()

    def _train_on_synthetic(self):
        texts, labels = [], []
        for category, keywords in CATEGORY_KEYWORDS.items():
            for _ in range(20):
                texts.append(" ".join(np.random.choice(keywords, size=min(len(keywords), 5), replace=True)))
                labels.append(category)
        self.pipeline.fit(texts, labels)
        self.trained = True

    def classify(self, job_description: str) -> dict:
        if not self.trained:
            return {"category": "Unknown", "confidence": 0.0}
        proba = self.pipeline.predict_proba([job_description])[0]
        classes = self.pipeline.classes_
        top_idx = int(np.argmax(proba))
        return {
            "category": classes[top_idx],
            "confidence": round(float(proba[top_idx]), 3),
            "all_scores": {c: round(float(p), 3) for c, p in zip(classes, proba)},
        }