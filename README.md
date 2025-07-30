# PubMed Paper Fetcher

A Python CLI tool to fetch PubMed papers based on a user-defined query and identify papers with at least one author affiliated with a **pharmaceutical or biotech company** (i.e., non-academic). Results are saved in CSV format. You have two options to get the results, either clone this repository and run this codebase via poetry or download the package from testpypi and use it.

---

## Code Organization

```
pubmed_paper_fetcher/
├── pubmed_fetcher/        # Core logic module
│   ├── api.py             # Handles PubMed API requests
│   ├── parser.py          # Parses XML returned from PubMed
│   ├── filters.py         # Heuristics to detect non-academic authors
│   ├── exporter.py        # Outputs results to CSV
│
├── cli/
│   └── main.py            # CLI interface entrypoint
│
├── pyproject.toml         # Poetry config (dependencies, packaging)
├── README.md              # You're reading it!
```

---

## Installation & Usage

### Requirements

- Python **3.10 or later**
- [Poetry](https://python-poetry.org/docs/) for packaging

### Install Dependencies

```bash
poetry install
```

### Run the CLI

```bash
# From the root of the project:
poetry run get-papers-list "covid" -f results.csv
```

### CLI Options

```bash
usage: get-papers-list.cmd [-h] [-d] [-f FILE] query

Fetch PubMed papers with non-academic authors.

positional arguments:
  query                 PubMed query string

options:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug output
  -f FILE, --file FILE  Output CSV file name
```

---

## Heuristics for Non-Academic Detection

An author is flagged as "non-academic" if their affiliation:

- Does **not** contain academic keywords (e.g., university, institute, hospital)

Matching is done using [`rapidfuzz`](https://github.com/maxbachmann/RapidFuzz).

---

## Tools, Libraries & LLMs Used

- [`requests`](https://docs.python-requests.org/): For HTTP calls to the PubMed API
- [`rapidfuzz`](https://github.com/maxbachmann/RapidFuzz): For fuzzy matching company/affiliation names
- [`argparse`](https://docs.python.org/3/library/argparse.html): For CLI argument parsing
- [`Poetry`](https://python-poetry.org/): Dependency management and packaging
- [`ChatGPT`](https://chatgpt.com/): Primarily for understanding and generating the poetry toml file, generating the academic keyword list in English and other languages, providing instructions for publishing the module on testpypi.
---

## Using the published library

The tool is published to [Test PyPI](https://test.pypi.org/) and can be installed with:

```bash
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple \
            pubmed-paper-fetcher-varunsingh3000==0.1.4
```
Note: The extra index part of the command is added to ensure other libraries such as rapidfuzz can be installed from the main index.

```bash
get-papers-list "covid" -f result.csv -d
```

---

## PubMed API Reference

# The following links provide access to the Pubmed APIs for developers

- https://pmc.ncbi.nlm.nih.gov/tools/developers/
- https://pmc.ncbi.nlm.nih.gov/tools/get-pmcids/
- https://pmc.ncbi.nlm.nih.gov/tools/get-metadata/

---

## License

MIT License
