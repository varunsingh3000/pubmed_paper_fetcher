import csv
from typing import List, Dict

def export_to_csv(papers: List[Dict], filename: str) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "PubmedID", "Title", "Publication Date",
            "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
        ])
        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)
