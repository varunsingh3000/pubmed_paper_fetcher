import argparse
from pubmed_fetcher.api import fetch_pubmed_ids, fetch_pubmed_details
from pubmed_fetcher.parser import parse_pubmed_xml
from pubmed_fetcher.filters import extract_company_authors, has_non_academic_author
from pubmed_fetcher.exporter import export_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name")

    args = parser.parse_args()

    ids = fetch_pubmed_ids(args.query, args.debug)
    xml_data = fetch_pubmed_details(ids, args.debug)
    raw_papers = parse_pubmed_xml(xml_data)

    filtered = []
    for paper in raw_papers:
        if has_non_academic_author(paper["Authors"]):
            names, companies, email = extract_company_authors(paper["Authors"])
            filtered.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": "; ".join(names),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email,
            })

    if args.file:
        export_to_csv(filtered, args.file)
        print(f"Results saved to {args.file}")
    else:
        for row in filtered:
            print(row)

if __name__ == "__main__":
    main()

# https://pmc.ncbi.nlm.nih.gov/tools/developers/
# https://pmc.ncbi.nlm.nih.gov/tools/get-pmcids/
# https://pmc.ncbi.nlm.nih.gov/tools/get-metadata/

# poetry install
# poetry run get-papers-list "covid" --debug --file covid.csv


# poetry version patch
# poetry build
# poetry publish --build -r test-pypi

# pip install --index-url https://test.pypi.org/simple/ \
#             --extra-index-url https://pypi.org/simple \
#             pubmed-paper-fetcher-varunsingh3000==0.1.4


# source myenv/Scripts/activate