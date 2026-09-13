import re


def clean_text(text):
    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Keep only letters, numbers and spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip().lower()


if __name__ == "__main__":
    sample = "<p>Python Developer - https://example.com</p>"
    print(clean_text(sample))
