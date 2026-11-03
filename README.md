# US entry-labeled software job listings

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23917034.svg)](https://doi.org/10.5281/zenodo.23917034)

Research by **Global Software Companies**. Version **2026-10-12b**.

Documentation, downloads and citation: [www.globalsoftwarecompanies.com/research-data/#software-job-listings-dataset](https://www.globalsoftwarecompanies.com/research-data/#software-job-listings-dataset). Used in: [Do You Need a Degree for an Entry-Level Software Job? We Checked 2,517 Listings](https://www.globalsoftwarecompanies.com/do-you-need-a-degree-entry-level-software-jobs/).

Also available on [Zenodo](https://doi.org/10.5281/zenodo.23917034), [Kaggle](https://www.kaggle.com/datasets/globalsoftwarecompan/us-entry-level-software-job-listings) and [Hugging Face](https://huggingface.co/datasets/GlobalSoftwareCompanies/us-entry-level-software-job-listings).

Annotations of selected US-labeled LinkedIn software job listings posted from January to August 2026: experience, skills, AI use, applicant projects, education, training, working conditions, hiring assessments and named technologies.

`jobs.csv` contains **2,518 listing records** and 75 columns: **2,517 retained for US analysis** and one excluded record with conflicting country information. `technologies.csv` contains **32,271 technology mentions** and five columns. Select `inclusion_status=retained`, then join technologies on `job_id`. Count distinct listings when measuring how often a technology appears; a listing can name the same technology in more than one context.

## Selection and method

The initial screen selected 5,625 US-labeled records dated 1 January–31 August 2026 with an Entry level seniority label. Titles had to contain `software` and at least one of `developer`, `engineer` or `programmer`, and none of `instructor`, `tutor`, `sales`, `recruiter`, `senior`, `manager` or `director`. Matching used case-insensitive literal substrings; no employment-type filter was applied.

Full-description review selected ordinary software-development roles whose lowest accepted qualification route required up to two professional years, or had no stated required numeric minimum. Occupation, geography and contradictory-role checks also applied. Qualified cases retained after review remain flagged in their notes. Internship vacancies, training placements and specialist AI-evaluation or model-development roles were outside the main cohort. A platform entry-level label is not proof of junior status; `entry_level_basis` records the supporting evidence.

Annotations were AI-assisted under written rules, with additional source checks and research decisions for conflicting cases. A GSC researcher checked about 1 in 5 of the AI classifications by hand and reviewed the edge cases those checks identified; this is a spot check, not a measured accuracy rate. Required, preferred, optional, duty, company and assessment contexts remain distinct. Three experience values are explicitly research-coded, and a stated duration counts as a professional minimum only when the listing presents it as professional or work experience; see [FIELD-GUIDE.md](FIELD-GUIDE.md). Notes are concise and can be terse.

Deduplication removed 458 repeats. It matched identical trimmed descriptions plus advertiser, title, location and inclusion disposition; advertiser/title/location matching ignored case and repeated whitespace. The earliest valid posting timestamp selected the representative, with the lowest numeric listing ID breaking ties. Different locations and edited descriptions remain separate. Use `same_text_group_id` or `advert_family_id` to explore repeated-description sensitivity.

## Interpretation

Most listings were posted in July and August 2026; earlier months are thinly covered, so the data don't support trends over time. These are selected listings, not a representative measure of the US jobs market or verified unique vacancies. Posting dates are recorded metadata; they do not establish hiring, vacancy creation or posting lifetimes. URLs may expire. Blank numbers are unknown, and `not_stated` does not mean absent. Broad indicators do not make every mentioned skill mandatory. Detailed technology identities, contexts and nested qualifiers may contain errors; unresolved findings remain visible. Advertised requirements do not measure applicant ability or hiring outcomes.

The [field guide](FIELD-GUIDE.md) defines every column and the structured cells. CSVs use UTF-8; some cells contain JSON. `manifest.json` records file hashes and row/column counts. Original listing descriptions and contact details are not included.

[REPRODUCE.md](REPRODUCE.md) and `reproduce.py` recompute the figures in GSC's articles on degree requirements (#3), citizenship, clearance and sponsorship requirements (#4) and the languages and tools listings name (#6).

## License and citation

The GSC contribution is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), allowing reuse, adaptation and redistribution, including commercially, with attribution. See [LICENSE.md](LICENSE.md).

> Global Software Companies (2026). *US entry-labeled software job listings*. Version 2026-10-12b. https://doi.org/10.5281/zenodo.23917034. Documentation: https://www.globalsoftwarecompanies.com/research-data/#software-job-listings-dataset. CC BY 4.0.

Credit Global Software Companies, preferably linking [the dataset's page](https://www.globalsoftwarecompanies.com/research-data/#software-job-listings-dataset); retain the license notice and identify modifications.
