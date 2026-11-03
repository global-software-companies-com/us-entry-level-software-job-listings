# Job dataset field guide

`jobs.csv` has one representative per matched description/advertiser/title/location/inclusion group. Filter `inclusion_status=retained` for US analysis and join `technologies.csv` on `job_id`. Dates and URLs belong to that representative. Group IDs identify repeated text or listing families, not verified unique vacancies.

## Status and experience values

Most skill, education, training and assessment indicators use `explicit` (source evidence), `not_stated` (no qualifying evidence recorded), `unresolved` (uncertain interpretation) or `not_available` (insufficient source). `ai_context=company_only` concerns the employer rather than the applicant or role. AI-assisted development and applicant-project evidence use `positive`, `unresolved` and `not_stated`; positive can include preferred or optional evidence. Applicant-project positives concern applicant portfolios, academic/personal/open-source projects or competitions, rather than routine employer project delivery.

`entry_level_basis` distinguishes `title_explicit`, `body_explicit`, `numbered_entry_level` (supported numbered entry role), `academic_internship_route`, `metadata_only` and `no_junior_evidence` (no qualifying independent role signal). These are evidence bases, not proficiency ratings.

Read `minimum_professional_years` with `experience_status`, `minimum_operator` and `experience_notes`:

| Experience status | Interpretation |
| --- | --- |
| `quantified_required` | Recorded required professional minimum across accepted routes. |
| `preferred_only` | Duration appears only as preferred; required numeric minimum is blank. |
| `not_stated` | No unavoidable numeric professional minimum established; blank is not zero. |
| `ambiguous` | Exact minimum is uncertain; numeric value remains blank. |
| `research_coded` | Declared research convention; numeric value is not an employer-stated universal minimum. |

A duration tied to a language, tool, platform or one area of software work (for example backend, embedded, iOS or test automation) counts as a professional minimum only when the listing states it as professional, industry or work experience, or when it concerns software development as a whole. Otherwise the status is `ambiguous` and the duration stays in `experience_notes`.

Three rows use `research_coded`. Two assign one year to required, unquantified entry-level engineering experience on a master's route, preserving the alternative bachelor's route requiring two related engineering years. One assigns the lower endpoint of an ideal-candidate 1–4-year production-code range; its mandatory force and professional scope remain uncertain. Report coded values separately from source-stated minima.

`>=` is an inclusive bound; `>` is strict. Operators are recorded where the listing's wording for the controlling duration is explicitly inclusive or strict, such as "2+ years", "at least", "minimum of", "or more", a range such as "1–3 years", or "more than". A bare "2 years" leaves the operator blank. A blank operator was not established and must not be assumed inclusive. Durations stated in months are converted to years and rounded to three decimals. Preferred years, technology durations and degree/project alternatives do not automatically establish a professional minimum or zero. A retained listing can have an ambiguous experience field. `whole_record_hold`, if present, would mean pending eligibility; `excluded_from_us_analysis` records a completed exclusion, with the reason in `research_notes`.

Blank numeric values and JSON `null` mean unknown/not established. `not_stated` is not confirmed absence. Unknown sponsorship is not refusal; remote wording is not worldwide eligibility. Unstated assessment payment is not evidence of an unpaid task. Interview AI policy differs from workplace AI policy.

## Fields

### jobs.csv

One representative of an exact-description/advertiser/title/location group within an inclusion disposition; not a verified unique vacancy.

| Field | Meaning |
| --- | --- |
| `job_id` | Stable source listing ID of the selected representative. |
| `job_title` | Advertised role title |
| `advertiser_name` | Posting organization; may be recruiter or intermediary |
| `advertised_location` | Recorded advertised location; not independently verified |
| `posted_date` | Recorded posting timestamp of the earliest selected representative; not acquisition time, a vacancy count or a complete posting interval. |
| `job_url` | Original listing URL, which may later expire |
| `entry_level_basis` | Explicit title/body, supported numbered entry role, academic/internship route, metadata-only or no qualifying independent junior evidence |
| `experience_status` | Source-stated quantified required, preferred only, not stated, ambiguous, or explicitly research-defined research_coded minimum |
| `minimum_professional_years` | Source-supported professional minimum for quantified_required; research-defined numeric value for research_coded. Read status, notes, bounds and alternatives |
| `minimum_operator` | Inclusive or strict source threshold for quantified_required; >= is the declared coded threshold for research_coded. Missing is not assumed inclusive |
| `experience_notes` | Current experience qualifications, preserving ranges, caps and alternative routes |
| `inclusion_status` | retained, whole_record_hold or excluded_from_us_analysis; select retained for US analyses, and read research_notes for the exclusion reason |
| `software_testing` | Software test knowledge, planning, execution or automation |
| `debugging` | Software debugging, defect diagnosis and troubleshooting |
| `code_review` | Code, peer or pull-request review |
| `existing_code_work` | Maintaining, understanding, refactoring or migrating existing software |
| `development_workflow` | Version control, builds, CI/CD, APIs, deployment, release practices, documentation or developer tooling |
| `communication_collaboration` | Substantive communication, teamwork, requirements gathering and stakeholder interaction |
| `ai_context` | General AI evidence; distinguish company-only mentions |
| `ai_ml_development` | AI/ML model or algorithm knowledge, development, training or evaluation |
| `ai_integration` | Integrating or consuming AI services/models/features |
| `ai_assisted_development` | Conservative reviewed substantive assisted-development claim view |
| `ai_output_checking` | Explicit checking of generated artifacts; preserve coding-assistant versus product-model output target in detail |
| `ai_work_security_provenance` | Privacy, security or provenance explicitly tied to AI-assisted work |
| `programming_languages` | Named programming, query, scripting or markup languages |
| `frameworks_libraries` | Named libraries, frameworks or platform SDKs |
| `data_work` | Databases, storage, querying, modeling, pipelines, data quality or analytics |
| `cloud_infrastructure` | Cloud infrastructure, containers, infrastructure-as-code or provider/service knowledge and duties |
| `software_security` | Technical software or system security knowledge and practices |
| `computing_foundations` | Explicit algorithms, data structures, concurrency, OS/network concepts or generic computing foundations |
| `software_design` | Design patterns, architecture decisions, decomposition, interfaces or explicit technical trade-offs |
| `production_operations` | Live-service operation, production support, monitoring, alerting, incidents or reliability/fault-tolerance work |
| `performance_optimization` | Profiling, bottlenecks, latency, throughput, scaling or resource optimization |
| `embedded_systems` | Firmware, drivers, real-time systems, physical interfaces, controls or hardware/software integration |
| `safety_assurance` | Safety-critical software context, formal assurance, certification evidence or qualification traceability |
| `product_problem_solving` | User discovery, problem definition, scoping, solution choices or technical/user/business trade-offs |
| `education_qualifications` | Evidence of education qualifications and alternatives |
| `education_details` | Stated level, subject, completion/graduation conditions and alternatives with qualification context |
| `applicant_project_evidence` | Conservative reviewed applicant qualification project/portfolio/competition claim |
| `applicant_project_details` | Accepted applicant work type, qualification/alternative context and material unresolved interpretation |
| `employer_training` | Employer-offered training, mentoring, pairing, onboarding or education support |
| `training_details` | Recorded support formats, scope and material qualifications |
| `work_arrangement` | Stated remote/hybrid/on-site arrangement with material qualifications |
| `work_authorization` | Stated right-to-work, citizenship or authorization conditions |
| `visa_sponsorship` | Stated availability, restriction or condition of sponsorship |
| `security_clearance` | Stated clearance level and already-held versus obtainable timing |
| `work_conditions_notes` | Concise relevant locality, office cadence, travel, relocation, on-call, timing or conflict qualifications |
| `hiring_assessment` | Recorded evidence of a selection interview/test/task/work demonstration; background, criminal, credit, drug and reference checks, other pre-employment screening, and application documents such as CVs or cover letters are not counted |
| `assessment_details` | Concise format/task, duration and stated payment with units, currency and relevant conditions |
| `assessment_ai_policy` | Stated AI-use allowance/requirement/restriction/prohibition, including target task and disclosure |
| `skill_details` | Specific skill practices and evidence statements with context, sign and meaningful alternatives |
| `role_context` | Source-recorded role/platform specialty, employer industry and separately qualified domain-background conditions |
| `work_expectations` | Recorded independence/guidance, initiative, problem-solving, ambiguity and learning expectations |
| `research_notes` | Short plain-language notes on problems in the listing (conflicting title, body or location details, template or truncated text), why a doubtful listing is retained or excluded, and research-coded values; blank when none apply |
| `same_text_group_id` | Same trimmed description text, regardless of advertiser/title/location/date |
| `advert_family_id` | Same description plus matching case/whitespace-normalized advertiser and title |

### Classification columns

The last 19 columns hold GSC's classification for its articles. They are blank for the excluded record. `explicit` means the listing states it; `not_stated` means it doesn't. Silence is not a "no".

**Citizenship, clearance and sponsorship.** Each unique listing text was coded by two independent AI coders under written rules, and a third decided disagreements (46 of 1,153 texts). The three sponsorship columns were then coded again under one rule for partial statements: every text mentioning sponsorship or visas (398) was coded by two independent AI coders, and a third decided disagreements and uncertain cases. The coders worked from the eligibility lines recorded in `work_authorization`, `visa_sponsorship` and `security_clearance` and the sentences of the listing body that mention these topics. Job titles alone don't count. Equal-opportunity wording is ignored, and citizenship is never inferred from a clearance.

| Column | Meaning |
| --- | --- |
| `us_citizenship_required` | Requires US citizenship. "Citizen or permanent resident", "U.S. person" and "authorized to work" don't count |
| `citizen_pr_or_us_person_required` | Requires citizenship or permanent residence or protected status ("U.S. person" under export rules). `not_stated` when citizenship alone is required |
| `clearance_required_at_hire` | A security clearance the applicant must already hold or have before starting |
| `clearance_required_after_hire` | A clearance the new hire must obtain, or "active or able to obtain". `not_stated` when one must already be held |
| `clearance_preferred_only` | A clearance mentioned only as preferred, with none required |
| `public_trust` | A Public Trust designation; never counted as a clearance |
| `sponsorship_unavailable` | The listing rules out sponsorship for all applicants or for some routes or visa types (for example, no new H-1B petitions), or applicants must not need sponsorship |
| `sponsorship_unavailable_future` | As above, and the wording covers future sponsorship or visa transfers |
| `sponsorship_available` | Sponsorship is offered or will be considered for at least some applicants, routes or visa types. A listing can have both this and `sponsorship_unavailable` (for example, transfers supported but no new petitions) |
| `required_clearance_level` | Highest required level: `confidential`, `secret`, `top_secret`, `ts_sci`, `ts_sci_poly` (SCI with a polygraph) or `unspecified`; blank when no clearance is required |
| `work_authorization_stated` | Applicants must be authorized to work in the US (any wording) |
| `opt_cpt_mentioned` | The listing mentions OPT, CPT or STEM OPT |

**Education.** Classified by rule from `education_details`, with a hand-checked table for years accepted in place of a degree, and a search of the saved listing text for the last three columns.

| Column | Meaning |
| --- | --- |
| `education_requirement` | `degree_required_no_alternative`, `degree_or_alternative` (a degree or a stated alternative, often experience), `degree_preferred_only`, `high_school_or_ged_only`, `no_requirement_stated` or `other_or_unclear` |
| `lowest_required_degree` | Lowest degree level accepted when a degree is required: `associate`, `unspecified_degree`, `bachelor`, `master` or `doctorate` |
| `degree_alternative_type` | For `degree_or_alternative`, the main alternative, taken in this order: `years` (a stated number of years), `high_school_or_ged_route`, `credential_or_training`, `projects_internships_coursework`, `experience` (unquantified) or `unspecified` ("or equivalent") |
| `degree_alternative_years` | Fewest years of experience accepted in place of the degree; `ratio` for year-for-year substitution with no fixed total |
| `bootcamp_mentioned` | The listing text mentions a coding bootcamp anywhere |
| `self_taught_mentioned` | The listing text mentions being self-taught |
| `degree_explicitly_downplayed` | The listing says in so many words that a degree isn't needed or matters less |

### technologies.csv

One named technology mention in a listing evidence context; reuse job_id. Exact duplicate rows are removed. The intended scope covers named technologies and standards; credentials, delivery methodologies and generic skill categories are excluded.

| Field | Meaning |
| --- | --- |
| `job_id` | Reuse the listing identifier in jobs.csv |
| `technology_name` | Resolved standard name or visibly unresolved source name |
| `technology_kind` | Recorded language/framework/library/tool/service/product kind |
| `technology_context` | Required/preferred/optional/duty/training/company or other recorded context |
| `technology_notes` | Concise material alternatives/examples, uncertainty, learning/proficiency qualifications or versions; otherwise blank |

## Structured cells

Detail columns contain JSON lists or objects. Parse these as JSON after reading the CSV. A fact commonly has `attribute`, `value`, `context`, `relationship` and an optional analyst's `note`, which can be terse; optional `scope` and `unit` qualify its meaning. A status-only object records that no usable fact was established. Empty lists contain no recorded detail.

Skill observations use `categories`, `practices`, `context` and `relationship`. `practices` uses a category prefix and readable practice name, such as `TS.unit_testing`; occasional entries are plain descriptions. `artifact_scope` distinguishes `coding_assistant_output`, `product_model_output`, `unspecified` and an unestablished null value. Broad output-checking evidence is not necessarily checking a coding assistant's output.

`same_condition` links facts in a shared requirement or route; `technologies_in_same_condition` links named technologies. `accepted_routes` and `universal_requirements` preserve alternative and common conditions. Applicant-project objects carry `current_status`, `observations` and `accepted_evidence_facts`; training details may include `formats`.

Current row indicators and explicit `current_*_status` or `current_category_statuses` summary keys govern older observation tags. `source_experience_status`, `source_minimum_professional_years` and `minimum_value_basis` distinguish source evidence from research coding. `research_coding_rule_id` labels the conventions explained above and requires no external lookup. Read notes for qualifications; an observation is not proof that every applicant must satisfy it.

Contexts are `required_qualification` (or `required`), `preferred_qualification`, `optional_qualification`, `responsibility`, `employer_training`, `company_context`, `selection_assessment`, `employment_condition`, `negated_qualification` and `unclear`. Relationships are `standalone`, `all_of` (combined), `one_of` (choice), `alternative_route`, `example` and `unclear`. Examples and choices do not require every listed item.

### Category codes

| Code | Corresponding field |
| --- | --- |
| `TS` | `software_testing` |
| `DB` | `debugging` |
| `CR` | `code_review` |
| `EM` | `existing_code_work` |
| `WF` | `development_workflow` |
| `CO` | `communication_collaboration` |
| `ML` | `ai_ml_development` |
| `AI` | `ai_integration` |
| `AT` | `ai_assisted_development` |
| `AV` | `ai_output_checking` |
| `PR` | `ai_work_security_provenance` |
| `LANG` | `programming_languages` |
| `FRAME` | `frameworks_libraries` |
| `DATA` | `data_work` |
| `CLOUD` | `cloud_infrastructure` |
| `SEC` | `software_security` |
| `FUND` | `computing_foundations` |
| `DESIGN` | `software_design` |
| `OPS` | `production_operations` |
| `PERF` | `performance_optimization` |
| `EMBED` | `embedded_systems` |
| `ASSURE` | `safety_assurance` |
| `PRODUCT` | `product_problem_solving` |
| `DEG` | `education_qualifications` |
| `PORT` | `applicant_project_evidence` |
| `TRAIN` | `employer_training` |
| `EXP` | `experience_status` |

### Technologies

`technology_kind` records language, framework, library, runtime, database, operating system, protocol, standard, cloud provider/service, SDK, developer/infrastructure/testing tool, hardware, AI framework/model/assistant, other or unresolved identity. An unresolved name is not a confirmed product. Preserve meaningful versions and identity qualifications in `technology_notes`.

`technology_context` uses the context values above. Multiple rows can record different contexts within one listing. Notes preserve alternatives, examples and learning/proficiency qualifications; technology mentions do not establish universally required expertise.
