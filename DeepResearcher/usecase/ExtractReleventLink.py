import re

def extract_links_from_summary(summary_text):
    pattern = r"Recommended link:\s*(https?://\S+)"
    links = re.findall(pattern, summary_text)
    return links
