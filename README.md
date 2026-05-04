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
| `SES_Completion_Analysis_2020_24.ipynb` | Jupyter notebook with Kruskal-Wallis tests and Dunn's pairwise post-hoc analysis |

**Note:** The underlying dataset contains student-level completion records
and is not included in this repository.

---

## Environment

**Python:** 3.14.4

**Jupyter Components:**

| Component | Version |
|-----------|---------|
| jupyter-core | 5.9.1 |
| jupyter-client | 8.8.0 |
| ipykernel | 7.2.0 |

**Packages:**

```
asttokens               3.0.1
colorama                0.4.6
comm                    0.2.3
contourpy               1.3.3
cycler                  0.12.1
debugpy                 1.8.20
decorator               5.2.1
et-xmlfile              2.0.0
executing               2.2.1
fonttools               4.62.1
ipykernel               7.2.0
ipython                 9.13.0
ipython-pygments-lexers 1.1.1
jedi                    0.20.0
jupyter-client          8.8.0
jupyter-core            5.9.1
kiwisolver              1.5.0
matplotlib              3.10.9
matplotlib-inline       0.2.1
nest-asyncio            1.6.0
numpy                   2.4.4
openpyxl                3.1.5
packaging               26.2
pandas                  3.0.2
parso                   0.8.7
patsy                   1.0.2
pillow                  12.2.0
pip                     26.1
platformdirs            4.9.6
prompt-toolkit          3.0.52
psutil                  7.2.2
pure-eval               0.2.3
pygments                2.20.0
pyparsing               3.3.2
python-dateutil         2.9.0.post0
pyzmq                   27.1.0
scikit-posthocs         0.12.0
scipy                   1.17.1
seaborn                 0.13.2
six                     1.17.0
stack-data              0.6.3
statsmodels             0.14.6
tornado                 6.5.5
traitlets               5.14.3
tzdata                  2026.2
wcwidth                 0.7.0
```
