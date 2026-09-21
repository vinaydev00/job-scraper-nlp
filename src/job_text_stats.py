def get_text_stats(text):
    """Return basic statistics for a job description."""

    if not text:
        return {
            "characters": 0,
            "words": 0,
            "lines": 0
        }

    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines())
    }


def is_description_valid(text, min_words=20):
    """Check whether a job description has enough text."""

    if not text:
        return False

    return len(text.split()) >= min_words
