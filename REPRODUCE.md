# Reproducing the figures in GSC's articles #3, #4 and #6

Article key: #3 degree requirements; #4 citizenship, clearance and sponsorship requirements; #6 languages and tools named in listings.

Run `python3 reproduce.py` in this folder (Python 3, standard library only). It recomputes the figures below from `jobs.csv` and `technologies.csv` and prints `OK` or `MISMATCH` for each.

## Rules

- **Listings:** rows with `inclusion_status = retained` (2,517).
- **Unique listings:** one row per `same_text_group_id`, the earliest `posted_date`, then the lowest `job_id` (2,186).
- **#3, degrees:** the `education_requirement`, `degree_alternative_type`, `degree_alternative_years`, `bootcamp_mentioned`, `self_taught_mentioned` and `degree_explicitly_downplayed` columns.
  - "Years stated in place of a degree" counts numeric `degree_alternative_years`; `ratio` is left out.
  - Project evidence is `applicant_project_evidence = positive`, split by `ai_assisted_development = positive`.
  - Employer-supported learning is `employer_training = explicit`.
- **#4, eligibility:** the 12 eligibility columns; `explicit` counts.
  - "At least one eligibility limit" means any of `us_citizenship_required`, `citizen_pr_or_us_person_required`, `clearance_required_at_hire`, `clearance_required_after_hire` or `sponsorship_unavailable`.
- **#6, languages and tools:** rows in `technologies.csv` for retained listings whose `technology_context` is `required_qualification`, `required`, `preferred_qualification` or `optional_qualification`. Count listings, not rows.
  - Languages are rows with `technology_kind = language`, with these spellings merged: JS→JavaScript, Java 11/Java 17→Java, Golang→Go, T-SQL/PL/SQL/PL/pgSQL/Microsoft SQL→SQL.
  - "Any AI coding tool or assistant" is `technology_kind = ai_assistant`, plus bare "Copilot" rows left `unresolved`, leaving out the advertiser's own recruiting agents (Jack and Jill).

Shares in the articles divide these counts by 2,517 listings (or 2,186 unique listings), or by the subgroup named in the article.

## Published values checked

| Figure | Value |
| --- | ---: |
| #3 education_requirement=degree_required_no_alternative (listings) | 993 |
| #3 education_requirement=degree_or_alternative (listings) | 747 |
| #3 education_requirement=high_school_or_ged_only (listings) | 12 |
| #3 education_requirement=degree_preferred_only (listings) | 97 |
| #3 education_requirement=no_requirement_stated (listings) | 638 |
| #3 education_requirement=other_or_unclear (listings) | 30 |
| #3 education_requirement=degree_required_no_alternative (unique) | 865 |
| #3 education_requirement=degree_or_alternative (unique) | 609 |
| #3 education_requirement=high_school_or_ged_only (unique) | 12 |
| #3 education_requirement=degree_preferred_only (unique) | 83 |
| #3 education_requirement=no_requirement_stated (unique) | 590 |
| #3 education_requirement=other_or_unclear (unique) | 27 |
| #3 degree_alternative_type=years | 83 |
| #3 degree_alternative_type=high_school_or_ged_route | 1 |
| #3 degree_alternative_type=credential_or_training | 33 |
| #3 degree_alternative_type=projects_internships_coursework | 13 |
| #3 degree_alternative_type=experience | 557 |
| #3 degree_alternative_type=unspecified | 60 |
| #3 years stated in place of a degree | 83 |
| #3 of which 4 or more | 60 |
| #3 of which 10 or more | 9 |
| #3 bootcamp_mentioned | 21 |
| #3 self_taught_mentioned | 5 |
| #3 degree_explicitly_downplayed | 4 |
| #3 project evidence (all listings) | 313 |
| #3 project evidence where AI-assisted development is mentioned | 95 |
| #3 project evidence in other listings | 218 |
| #3 employer-supported learning | 783 |
| #4 at least one eligibility limit (listings) | 939 |
| #4 at least one eligibility limit (unique) | 852 |
| #4 us_citizenship_required | 320 |
| #4 citizen_pr_or_us_person_required | 123 |
| #4 clearance_required_at_hire | 303 |
| #4 clearance_required_after_hire | 239 |
| #4 clearance_preferred_only | 18 |
| #4 public_trust | 28 |
| #4 sponsorship_unavailable | 251 |
| #4 sponsorship_unavailable_future | 116 |
| #4 sponsorship_available | 22 |
| #4 opt_cpt_mentioned | 29 |
| #4 any required clearance | 542 |
| #4 required_clearance_level=confidential | 1 |
| #4 required_clearance_level=secret | 250 |
| #4 required_clearance_level=top_secret | 41 |
| #4 required_clearance_level=ts_sci | 60 |
| #4 required_clearance_level=ts_sci_poly | 117 |
| #4 required_clearance_level=unspecified | 73 |
| #6 listings naming Python as a qualification | 1,156 |
| #6 listings naming Java as a qualification | 815 |
| #6 listings naming C++ as a qualification | 776 |
| #6 listings naming JavaScript as a qualification | 675 |
| #6 listings naming C# as a qualification | 562 |
| #6 listings naming any AI coding tool or assistant as a qualification | 131 |
