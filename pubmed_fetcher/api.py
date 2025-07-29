import requests
from typing import List

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_pubmed_ids(query: str, debug: bool = False) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 200,
    }
    response = requests.get(f"{BASE_URL}/esearch.fcgi", params=params)
    response.raise_for_status()
    data = response.json()
    # print(data)
    ids = data.get("esearchresult", {}).get("idlist", [])
    if debug:
        print(f"[DEBUG] Found {len(ids)} PubMed IDs")
    return ids

def fetch_pubmed_details(pubmed_ids: List[str], debug: bool = False) -> str:
    if not pubmed_ids:
        return ""
    ids_str = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml",
    }
    response = requests.get(f"{BASE_URL}/efetch.fcgi", params=params)
    response.raise_for_status()
    # print(response)
    if debug:
        print(f"[DEBUG] Retrieved XML for {len(pubmed_ids)} papers")
    return response.text
