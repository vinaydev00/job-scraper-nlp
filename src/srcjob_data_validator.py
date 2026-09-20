def validate_job_data(job):
    """Check if a scraped job contains the basic required fields."""

    required_fields = ["title", "company", "description"]

    for field in required_fields:
        if field not in job or not job[field]:
            return False

    return True


def clean_job_fields(job):
    """Remove extra spaces from common job fields."""

    cleaned = job.copy()

    for field in ["title", "company", "description", "location"]:
        if field in cleaned and isinstance(cleaned[field], str):
            cleaned[field] = " ".join(cleaned[field].split())

    return cleaned


def validate_and_clean_job(job):
    """Validate and clean a scraped job record."""

    if not validate_job_data(job):
        return None

    return clean_job_fields(job)
