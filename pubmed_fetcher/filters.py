from typing import List, Tuple, Dict
from rapidfuzz import fuzz


ACADEMIC_KEYWORDS = [
    # English
    "university", "institute", "college", "school", "academy", "faculty",
    "hospital", "graduate school",

    # Spanish
    "universidad", "instituto", "colegio", "escuela", "academia", "facultad",
    "hospital", "escuela de posgrado",

    # French
    "université", "institut", "collège", "école", "académie", "faculté",
    "hôpital", "école doctorale",

    # Dutch
    "universiteit", "instituut", "hogeschool", "school", "academie", "faculteit",
    "ziekenhuis", "graduate school",

    # German
    "universität", "institut", "hochschule", "schule", "akademie", "fakultät",
    "krankenhaus", "graduiertenschule"
]

def is_non_academic(affiliation: str, threshold: int = 85) -> bool:
    """
    Returns True if the affiliation is considered non-academic
    based on fuzzy matching against academic keywords.
    """
    affil = affiliation.lower()
    for keyword in ACADEMIC_KEYWORDS:
        score = fuzz.partial_ratio(keyword, affil)
        if score >= threshold:
            return False  # It resembles an academic affiliation
    return True  # No close match found → likely non-academic

def extract_company_authors(authors: List[dict]) -> Tuple[List[str], List[str], str]:
    names = []
    companies = []
    email = ""
    for author in authors:
        if is_non_academic(author["affiliation"]):
            names.append(author["name"])
            companies.append(author["affiliation"])
        if "@" in author.get("email", "") and not email:
            email = author["email"]
    return names, companies, email

def has_non_academic_author(authors: List[Dict]) -> bool:
    """Return True if any author has a non-academic affiliation."""
    return any(is_non_academic(a["affiliation"]) for a in authors)