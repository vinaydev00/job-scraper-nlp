# 🔍 Job Scraper NLP

> Automated job listing scraper with NLP-powered classification and skill extraction.

## Features
- Scrapes job listings from any HTML source
- Extracts required skills automatically
- Classifies jobs into categories using TF-IDF + Logistic Regression
- Detects salary ranges from unstructured text

## Quickstart
pip install -r requirements.txt
python -m src.scraper

## Architecture
HTML Source → JobScraper → JobListing → JobClassifier → Category + Skills

## Pipeline

1. Scrape job listings from configured sources.
2. Clean and normalize job descriptions.
3. Classify jobs using NLP.
4. Extract relevant technical skills.
5. Store and present structured job information.

## Key Technologies

- Python
- NLP
- Job Scraping
- Skill Extraction
- Text Classification
- REST/API Integration

- ## Project Highlights

- Automated job listing collection
- NLP-based job classification
- Automatic technical skill extraction
- End-to-end processing pipeline
- Modular source-code structure
