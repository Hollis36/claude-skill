# MCP Bio-Research Tools API Reference

Pre-installed MCP tools for accessing biomedical literature databases. Initialize with `/bio-research:start`.

---

## PubMed

Search biomedical and life sciences literature (36M+ citations).

| Tool | Description |
|------|-------------|
| `search_articles` | Search by keyword, author, date range |
| `get_article_metadata` | Get title, abstract, authors, journal, DOI |
| `find_related_articles` | Find papers related to a given PMID |
| `lookup_article_by_citation` | Find article from partial citation info |
| `convert_article_ids` | Convert between PMID, DOI, PMC IDs |
| `get_full_text_article` | Retrieve full text (when available) |
| `get_copyright_status` | Check open access / copyright status |

---

## bioRxiv / medRxiv

Access preprints (not yet peer-reviewed).

| Tool | Description |
|------|-------------|
| `search_preprints` | Find preprints by keyword, author, date |
| `get_preprint` | Get full details by DOI |
| `get_categories` | List subject categories |
| `search_published_preprints` | Find preprints now published in journals |
| `search_by_funder` | Find preprints by funding source |
| `get_content_statistics` | Submission volume stats |
| `get_usage_statistics` | Download/view stats |

---

## ChEMBL

Bioactive drug-like molecules database. Best for pharmaceutical/drug discovery reviews.

| Tool | Description |
|------|-------------|
| `compound_search` | Find by name, SMILES, or ChEMBL ID |
| `get_bioactivity` | IC50, EC50, Ki values |
| `target_search` | Find biological targets |
| `get_mechanism` | Drug mechanism of action |
| `drug_search` | Find approved drugs by indication |
| `get_admet` | ADMET pharmacokinetic properties |

---

## ClinicalTrials.gov

Registry of clinical studies worldwide. Best for clinical research and treatment comparison reviews.

| Tool | Description |
|------|-------------|
| `search_trials` | Search by condition, intervention, status |
| `get_trial_details` | Protocol, endpoints, locations |
| `search_by_sponsor` | Company/institution pipeline analysis |
| `search_investigators` | Find PIs and research sites |
| `analyze_endpoints` | Compare endpoints across trials |
| `search_by_eligibility` | Match patients by criteria |

---

## Open Targets

Drug target and disease association data. Best for target identification and disease mechanism reviews.

| Tool | Description |
|------|-------------|
| `search_entities` | Find targets, diseases, drugs |
| `query_open_targets_graphql` | Custom GraphQL queries |
| `batch_query_open_targets_graphql` | Batch queries |
| `get_open_targets_graphql_schema` | Explore available data |

---

## Multi-Database Search Workflow

```
Step 1: Broad search
  PubMed:  search_articles(query="your topic", max_results=100)
  bioRxiv: search_preprints(query="your topic", num_results=50)

Step 2: Verify preprint status
  bioRxiv: search_published_preprints(query="your topic")

Step 3: Deep dive on key papers
  PubMed: get_article_metadata(pmid="...")
  PubMed: get_full_text_article(pmid="...")
  PubMed: find_related_articles(pmid="...")

Step 4: Expand to specialized databases
  ChEMBL:         compound_search(...) / drug_search(...)
  ClinicalTrials: search_trials(...)
  Open Targets:   search_entities(...)

Step 5: Track funding and trends
  bioRxiv:        search_by_funder(...)
  bioRxiv:        get_content_statistics(...)
  ClinicalTrials: search_by_sponsor(...)
```
