"""End-to-end job scraping and classification pipeline."""

from src.scraper import JobScraper, JobListing
from src.classifier import JobClassifier
from src.skill_extractor import SkillExtractor

class JobPipeline:
    def __init__(self):
        self.scraper = JobScraper()
        self.classifier = JobClassifier()
        self.extractor = SkillExtractor()

    def process(self, job_description: str, title: str = "", company: str = "") -> dict:
        skills = self.extractor.extract(job_description)
        categories = self.extractor.get_categories(job_description)
        classification = self.classifier.classify(job_description)
        salary = self.scraper.extract_salary(job_description)

        return {
            "title": title,
            "company": company,
            "classification": classification,
            "skills": [{"name": s.name, "category": s.category, "frequency": s.frequency} for s in skills[:10]],
            "skill_categories": categories,
            "salary_range": salary,
            "total_skills_found": len(skills),
        }