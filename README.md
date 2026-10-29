# Synthetic Degree Completion Analysis (2020–2024)

**Entirely fictional data; no real student records or institutional results.**


## Run

```bash
pip install -r requirements.txt
python generate_synthetic_data.py
jupyter notebook synthetic_completion_analysis.ipynb
```

Run all notebook cells in order. Tables and plots are saved under `outputs/`.

The dataset is independently generated with a fixed random seed. It is not modeled on, fitted to, or sampled from an institutional dataset. Findings must not be interpreted as real university statistics or COVID effects.

## Distribution charts
The descriptive-statistics section exports 30 five-bin histograms and 30 boxplots (one for each degree-by-term subset). Set `SHOW_DISTRIBUTION_PLOTS = True` in the notebook to display them inline. No Shapiro-Wilk test is used.
