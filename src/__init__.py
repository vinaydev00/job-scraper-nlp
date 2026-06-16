"""
Job Scraper - Scrapes job listings and extracts structured data.
"""

import re
import requests
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class JobListing:
    title: str
    company: str
    location: str
    description: str
    skills_required: list = field(default_factory=list)
    salary_range: str = ""
    posted_date: str = ""
    source_url: str = ""

class JobScraper:
    SKILL_KEYWORDS = [
        "python", "javascript", "sql", "machine learning", "deep learning",
        "nlp", "docker", "kubernetes", "aws", "azure", "react", "node.js",
        "java", "golang", "rust", "spark", "kafka", "airflow", "dbt",
    ]

    def extract_skills(self, description: str) -> list:
        found = []
        desc_lower = description.lower()
        for skill in self.SKILL_KEYWORDS:
            if skill in desc_lower:
                found.append(skill.title())
        return found

    def extract_salary(self, text: str) -> str:
        patterns = [
            r"\$[\d,]+\s*-\s*\$[\d,]+",
            r"₹[\d,]+\s*-\s*₹[\d,]+",
            r"\d+\s*LPA",
            r"\d+k\s*-\s*\d+k",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group()
        return "Not specified"

    def parse_job_html(self, html: str, source_url: str = "") -> JobListing:
        """Parse raw HTML into a JobListing. Extend for specific job boards."""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        description = soup.get_text(separator=" ", strip=True)
        return JobListing(
            title=soup.find("h1").text if soup.find("h1") else "Unknown",
            company="Unknown",
            location="Unknown",
            description=description[:2000],
            skills_required=self.extract_skills(description),
            salary_range=self.extract_salary(description),
            posted_date=datetime.now().strftime("%Y-%m-%d"),
            source_url=source_url,
        )