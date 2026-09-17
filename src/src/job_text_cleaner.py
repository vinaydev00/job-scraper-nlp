import re


def clean_job_text(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def prepare_job(job):
    job["title"] = clean_job_text(job.get("title", ""))
    job["description"] = clean_job_text(job.get("description", ""))

    return job
