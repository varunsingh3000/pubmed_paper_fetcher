# pubmed-paper-fetcher

A command-line tool to fetch PubMed research papers with at least one author affiliated with a pharmaceutical or biotech company.

---

## Features

- Query PubMed using full syntax support
- Filter for **non-academic authors** (pharma/biotech) using heuristic and fuzzy matching
- Output results to CSV or print to console
- CLI with helpful flags for debugging and output customization
- Published as a reusable Python module via Poetry

---

## Use Case

This tool is helpful for:
- Competitive research teams
- Pharma intelligence analysts
- Bioinformatics workflows
- ML pipelines identifying industry-led research

---

## Installation

### From Test PyPI (for testing only):
```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-paper-fetcher
