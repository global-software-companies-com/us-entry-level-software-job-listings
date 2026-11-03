#!/usr/bin/env python3
"""Recompute figures from GSC's articles #3 (degrees), #4 (citizenship, clearance, sponsorship) and #6 (languages
and tools) from jobs.csv and technologies.csv, and compare them with the published values.

Run in this folder: python3 reproduce.py   (Python 3, standard library only)
"""
import collections
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "#3 education_requirement=degree_required_no_alternative (listings)": 993,
    "#3 education_requirement=degree_or_alternative (listings)": 747,
    "#3 education_requirement=high_school_or_ged_only (listings)": 12,
    "#3 education_requirement=degree_preferred_only (listings)": 97,
    "#3 education_requirement=no_requirement_stated (listings)": 638,
    "#3 education_requirement=other_or_unclear (listings)": 30,
    "#3 education_requirement=degree_required_no_alternative (unique)": 865,
    "#3 education_requirement=degree_or_alternative (unique)": 609,
    "#3 education_requirement=high_school_or_ged_only (unique)": 12,
    "#3 education_requirement=degree_preferred_only (unique)": 83,
    "#3 education_requirement=no_requirement_stated (unique)": 590,
    "#3 education_requirement=other_or_unclear (unique)": 27,
    "#3 degree_alternative_type=years": 83,
    "#3 degree_alternative_type=high_school_or_ged_route": 1,
    "#3 degree_alternative_type=credential_or_training": 33,
    "#3 degree_alternative_type=projects_internships_coursework": 13,
    "#3 degree_alternative_type=experience": 557,
    "#3 degree_alternative_type=unspecified": 60,
    "#3 years stated in place of a degree": 83,
    "#3 of which 4 or more": 60,
    "#3 of which 10 or more": 9,
    "#3 bootcamp_mentioned": 21,
    "#3 self_taught_mentioned": 5,
    "#3 degree_explicitly_downplayed": 4,
    "#3 project evidence (all listings)": 313,
    "#3 project evidence where AI-assisted development is mentioned": 95,
    "#3 project evidence in other listings": 218,
    "#3 employer-supported learning": 783,
    "#4 at least one eligibility limit (listings)": 939,
    "#4 at least one eligibility limit (unique)": 852,
    "#4 us_citizenship_required": 320,
    "#4 citizen_pr_or_us_person_required": 123,
    "#4 clearance_required_at_hire": 303,
    "#4 clearance_required_after_hire": 239,
    "#4 clearance_preferred_only": 18,
    "#4 public_trust": 28,
    "#4 sponsorship_unavailable": 251,
    "#4 sponsorship_unavailable_future": 116,
    "#4 sponsorship_available": 22,
    "#4 opt_cpt_mentioned": 29,
    "#4 any required clearance": 542,
    "#4 required_clearance_level=confidential": 1,
    "#4 required_clearance_level=secret": 250,
    "#4 required_clearance_level=top_secret": 41,
    "#4 required_clearance_level=ts_sci": 60,
    "#4 required_clearance_level=ts_sci_poly": 117,
    "#4 required_clearance_level=unspecified": 73,
    "#6 listings naming Python as a qualification": 1156,
    "#6 listings naming Java as a qualification": 815,
    "#6 listings naming C++ as a qualification": 776,
    "#6 listings naming JavaScript as a qualification": 675,
    "#6 listings naming C# as a qualification": 562,
    "#6 listings naming any AI coding tool or assistant as a qualification": 131
}
APPLICANT = {'required_qualification', 'required', 'preferred_qualification', 'optional_qualification'}
LANGUAGE_MERGE = {'JS': 'JavaScript', 'Java 11': 'Java', 'Java 17': 'Java', 'Golang': 'Go', 'T-SQL': 'SQL', 'PL/SQL': 'SQL',
                  'PL/pgSQL': 'SQL', 'Microsoft SQL': 'SQL', 'HTML5': 'HTML', 'CSS3': 'CSS', 'Visual Basic .NET': 'VB.NET'}
AI_NAMES = {'Claude Code', 'Cursor', 'GitHub Copilot', 'OpenAI Codex', 'Claude', 'Claude.ai', 'Claude Enterprise', 'ChatGPT',
            'Copilot', 'CoPilot', 'copilot', 'Microsoft Copilot', 'Gemini'}
NOT_APPLICANT_TOOLS = {'Jack AI recruiter', 'Jill AI recruiter', 'Jill (Jack & Jill recruiter)', 'Jack (Jack & Jill career agent)'}


def main():
    jobs = [r for r in csv.DictReader(open(HERE / 'jobs.csv', encoding='utf-8')) if r['inclusion_status'] == 'retained']
    best = {}
    for r in jobs:  # unique listings: one per same_text_group_id, earliest posted_date, then lowest job_id
        key = (r['posted_date'], int(r['job_id']))
        g = r['same_text_group_id']
        if g not in best or key < best[g][0]:
            best[g] = (key, r)
    uniq = [r for _, r in best.values()]
    got = {}
    for basis, rows in (('listings', jobs), ('unique', uniq)):
        for cat, k in collections.Counter(r['education_requirement'] for r in rows).items():
            got[f'#3 education_requirement={cat} ({basis})'] = k
    alt = [r for r in jobs if r['education_requirement'] == 'degree_or_alternative']
    for t, k in collections.Counter(r['degree_alternative_type'] for r in alt).items():
        got[f'#3 degree_alternative_type={t}'] = k
    years = [float(r['degree_alternative_years']) for r in alt if r['degree_alternative_years'] not in ('', 'ratio')]
    got['#3 years stated in place of a degree'] = len(years)
    got['#3 of which 4 or more'] = sum(y >= 4 for y in years)
    got['#3 of which 10 or more'] = sum(y >= 10 for y in years)
    for col in ('bootcamp_mentioned', 'self_taught_mentioned', 'degree_explicitly_downplayed'):
        got[f'#3 {col}'] = sum(r[col] == 'explicit' for r in jobs)
    ai = [r for r in jobs if r['ai_assisted_development'] == 'positive']
    other = [r for r in jobs if r['ai_assisted_development'] != 'positive']
    project = lambda r: r['applicant_project_evidence'] == 'positive'
    got['#3 project evidence (all listings)'] = sum(map(project, jobs))
    got['#3 project evidence where AI-assisted development is mentioned'] = sum(map(project, ai))
    got['#3 project evidence in other listings'] = sum(map(project, other))
    got['#3 employer-supported learning'] = sum(r['employer_training'] == 'explicit' for r in jobs)
    e = lambda r, c: r[c] == 'explicit'
    limit = lambda r: any(e(r, c) for c in ('us_citizenship_required', 'citizen_pr_or_us_person_required',
                                             'clearance_required_at_hire', 'clearance_required_after_hire', 'sponsorship_unavailable'))
    for basis, rows in (('listings', jobs), ('unique', uniq)):
        got[f'#4 at least one eligibility limit ({basis})'] = sum(map(limit, rows))
    for col in ('us_citizenship_required', 'citizen_pr_or_us_person_required', 'clearance_required_at_hire',
                'clearance_required_after_hire', 'clearance_preferred_only', 'public_trust', 'sponsorship_unavailable',
                'sponsorship_unavailable_future', 'sponsorship_available', 'opt_cpt_mentioned'):
        got[f'#4 {col}'] = sum(e(r, col) for r in jobs)
    got['#4 any required clearance'] = sum(e(r, 'clearance_required_at_hire') or e(r, 'clearance_required_after_hire') for r in jobs)
    for level, k in collections.Counter(r['required_clearance_level'] for r in jobs if r['required_clearance_level']).items():
        got[f'#4 required_clearance_level={level}'] = k
    ids = {r['job_id'] for r in jobs}
    tech = [t for t in csv.DictReader(open(HERE / 'technologies.csv', encoding='utf-8'))
            if t['job_id'] in ids and t['technology_context'] in APPLICANT]
    langs = collections.defaultdict(set)
    any_ai = set()
    for t in tech:
        if t['technology_kind'] == 'language':
            langs[LANGUAGE_MERGE.get(t['technology_name'], t['technology_name'])].add(t['job_id'])
        name, kind = t['technology_name'], t['technology_kind']
        if name in NOT_APPLICANT_TOOLS:
            continue
        if kind == 'ai_assistant' or (kind == 'unresolved' and name.lower() == 'copilot' and name in AI_NAMES):
            any_ai.add(t['job_id'])
    for lang in ('Python', 'Java', 'C++', 'JavaScript', 'C#'):
        got[f'#6 listings naming {lang} as a qualification'] = len(langs[lang])
    got['#6 listings naming any AI coding tool or assistant as a qualification'] = len(any_ai)

    ok = bad = 0
    for key, want in EXPECTED.items():
        have = got.get(key, 0)
        same = have == want
        ok += same
        bad += not same
        print(f"{'OK      ' if same else 'MISMATCH'} {key:<75} {have}  (published {want})")
    print(f'\n{ok} figures reproduced, {bad} mismatches. Shares: divide by {len(jobs)} listings or {len(uniq)} unique listings.')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
