"""Advanced skill extractor using pattern matching and taxonomy."""

import re
from dataclasses import dataclass

@dataclass
class ExtractedSkill:
    name: str
    category: str
    frequency: int

SKILL_PATTERNS = {
    "Python": "programming",
    "JavaScript": "programming",
    "SQL": "database",
    "Machine Learning": "ai_ml",
    "Deep Learning": "ai_ml",
    "Docker": "devops",
    "Kubernetes": "devops",
    "AWS": "cloud",
    "Azure": "cloud",
    "React": "frontend",
    "Node.js": "backend",
    "FastAPI": "backend",
    "Spark": "data_engineering",
    "Kafka": "data_engineering",
    "Airflow": "data_engineering",
    "NLP": "ai_ml",
    "TensorFlow": "ai_ml",
    "PyTorch": "ai_ml",
}

class SkillExtractor:
    def extract(self, text: str) -> list[ExtractedSkill]:
        found = {}
        for skill, category in SKILL_PATTERNS.items():
            pattern = re.compile(re.escape(skill), re.IGNORECASE)
            matches = pattern.findall(text)
            if matches:
                if skill in found:
                    found[skill].frequency += len(matches)
                else:
                    found[skill] = ExtractedSkill(skill, category, len(matches))
        return sorted(found.values(), key=lambda x: x.frequency, reverse=True)

    def get_categories(self, text: str) -> dict:
        skills = self.extract(text)
        categories = {}
        for skill in skills:
            if skill.category not in categories:
                categories[skill.category] = []
            categories[skill.category].append(skill.name)
        return categories