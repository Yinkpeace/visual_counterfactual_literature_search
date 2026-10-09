# Visual Counterfactual Literature Search

This repository provides code to reproduce the automated literature-search workflow used in our review paper, **Visual Counterfactual Explanations and Beyond: A systematic Review**. It retrieves literature on visual counterfactuals, removes duplicate records, and performs automatic screening with suggested categories for further review.

## Setup

Install Python 3.10 or later, open a terminal in this repository, and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

An internet connection is required for searching and downloading papers. If you use API credentials, set the corresponding environment variables: `OPENALEX_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY`, or `GITHUB_TOKEN`.

## Run the search

Search OpenAlex and conference paper lists from Paper Copilot:

```bash
python main.py search --output runs/visual
```

The search automatically retrieves all available result pages and screens the returned records. No publication-date cutoff is applied. Results may change as the sources are updated; the search log records the execution dates and retrieval status.

To also search Semantic Scholar and Crossref:

```bash
python main.py search --sources openalex conferences semantic-scholar crossref --output runs/visual-all-sources
```

Use a new or empty output folder for each run. If a search is incomplete, inspect `search_log.json` and rerun it in a new folder.

## Optional steps

Download available PDFs for candidate papers and records awaiting review:

```bash
python main.py download --input runs/visual/screening.csv --output runs/downloads
```

Repeat screening with evidence from the downloaded PDFs:

```bash
python main.py screen --input runs/visual/screening.csv --pdf-dir runs/downloads/pdfs --output runs/pdf-screened
```

Screen your own metadata CSV, containing at least a `title` column and preferably an `abstract` column:

```bash
python main.py screen --input records.csv --output runs/screened
```

Import and screen Web of Science full-record exports saved as tagged `.txt` files:

```bash
python main.py import-wos --input-dir exports --output runs/imported
```

For command options, run `python main.py --help` or `python main.py search --help`.

## Deduplication and merging across sources

Records from OpenAlex, conference lists, Semantic Scholar, and Crossref are merged automatically within the same search run. Duplicate matching uses DOI first, then normalized titles when the DOIs do not conflict. Matching ignores DOI URL prefixes and letter case, and ignores punctuation and spacing in titles.

For matched records, missing metadata is filled from the other source. Existing nonempty values are retained, and source names, query strings, and source record IDs are combined. Records with different explicit DOIs are kept separate even when their titles match. Publication versions with changed titles or different DOIs require manual checking.

Web of Science imports and separate search runs are processed independently. To merge them with other repositories or databases, combine their exported metadata into one CSV, aligning columns by name and keeping one header row. Preserve the `doi`, `title`, `source`, `query`, and `source_record_id` columns where available, then run:

```bash
python main.py screen --input combined_records.csv --output runs/merged
```

This deduplicates the combined records and applies the same visual-counterfactual screening rules. The resulting `screening.csv` retains the combined source information.

## Expected outputs

Files are saved in the folder specified by `--output`.

| File or folder | Contents |
| --- | --- |
| `search_log.json` | Search queries, sources, execution dates, retrieval counts, completion status, and errors. Created by `search`. |
| `retrieved.jsonl` | Retrieved metadata with source and query information. Created by `search`. |
| `screening.csv` | Deduplicated records with screening decisions, reasons, evidence excerpts, and suggested categories. |
| `candidates.csv` | Papers identified as potential visual-counterfactual studies. |
| `manual_review.csv` | Records requiring further assessment. |
| `downloads.csv` | PDF download outcomes, including missing links and failures. Created by `download`. |
| `pdfs/` | Successfully downloaded PDFs, named by record ID. Created by `download`. |

The `search`, `screen`, and `import-wos` commands produce the three screening CSV files. Automatic decisions and category suggestions require human verification before final inclusion in the review.
