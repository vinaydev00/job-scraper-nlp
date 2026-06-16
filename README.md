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