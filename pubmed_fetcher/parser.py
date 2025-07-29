import xml.etree.ElementTree as ET
from typing import List, Dict

def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    articles = []

    for article in root.findall(".//PubmedArticle"):
        data = {
            "PubmedID": article.findtext(".//PMID"),
            "Title": article.findtext(".//ArticleTitle"),
            "Publication Date": article.findtext(".//PubDate/Year") or "Unknown",
            "Authors": [],
        }
        
        for author in article.findall(".//Author"):
            last = author.findtext("LastName") or ""
            first = author.findtext("ForeName") or ""
            affil = author.findtext(".//AffiliationInfo/Affiliation") or ""
            email = ""
            if "@" in affil:
                email = affil.split()[-1] if "@" in affil.split()[-1] else ""

            # Skip if all fields are empty
            if not any([first, last, email, affil]):
                continue

            data["Authors"].append({
                "name": f"{first} {last}".strip(),
                "affiliation": affil,
                "email": email,
            })

        articles.append(data)
    # print(articles)
    return articles
