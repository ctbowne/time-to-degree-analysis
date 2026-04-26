# Time-to-Degree Analysis
**Ad hoc statistical study conducted for school deans, Claremont Graduate University**

Kruskal-Wallis tests with Dunn's pairwise post-hoc analysis on MA and PhD
completion times across 2020–2024, identifying statistically significant shifts
in Summer cohort completion patterns for both degree levels.

---

## Overview

This study examined whether median time-to-degree changed significantly across
graduation years (2020–2024) for MA and PhD students, broken out by graduation
term (Spring, Summer, Fall). The goal was to give school leadership a
statistically grounded answer to the question: *has it taken students longer
(or shorter) to complete their degrees over time?*

---

## Methods

**Step 1 — Kruskal-Wallis test (per degree × term combination)**
A nonparametric Kruskal-Wallis test was applied to each degree/term group
to test whether any significant difference in median completion time existed
across years. Nonparametric methods were used given the distribution of
time-to-degree data.

**Step 2 — Dunn's pairwise post-hoc test with Bonferroni correction**
For groups where the Kruskal-Wallis test returned p < 0.05, Dunn's test was
used to identify which specific year pairs drove the significant result.
Bonferroni correction was applied across all pairwise comparisons.

---

## Key Findings

Significant differences in median completion time were found only in
**Summer term** cohorts:

| Degree | Comparison | Change | Significant? |
|--------|-----------|--------|-------------|
| MA | 2020 vs 2021 | +0.34 years | Yes |
| MA | 2020 vs 2023 | +0.67 years | Yes |
| MA | 2023 vs 2024 | −0.34 years | Yes |
| PhD | 2022 vs 2023 | −5.00 years | Yes |

All Spring and Fall term differences were not statistically significant —
consistent with stable completion times or insufficient sample sizes to
detect change.

---

## Repository Contents

| File | Description |
|------|-------------|
| `time_to_degree_analysis.R` | R code for Kruskal-Wallis tests and Dunn's pairwise post-hoc analysis |

**Note:** The underlying dataset contains student-level completion records
and is not included in this repository.

---

## Tools & Packages

- **R** — `dplyr`, `stats`, `dunn.test`
- Kruskal-Wallis: `kruskal.test()`
- Dunn's post-hoc: `dunn.test()` with Bonferroni correction
