"""Generate wholly fictional completion records; never reads institutional data."""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 20261017
YEARS = range(2020, 2025)
SEASONS = ('Spring', 'Summer', 'Fall')
DEGREES = ('Masters', 'Research Doctorate')


def generate(seed=SEED):
    rng = np.random.default_rng(seed)
    rows = []
    # Independently chosen illustrative parameters, not estimated from real data.
    specs = {
        'Masters': {'base': 2.7, 'sigma': .37, 'count': 44},
        'Research Doctorate': {'base': 5.5, 'sigma': .40, 'count': 28},
    }
    for degree in DEGREES:
        for season in SEASONS:
            for year in YEARS:
                cfg = specs[degree]
                # Fictional seasonal and year effects produce interesting examples.
                seasonal = {'Spring': 1.00, 'Summer': 1.08, 'Fall': .96}[season]
                annual = 1 + .035 * (year - 2022)
                if degree == 'Masters' and season == 'Summer':
                    annual *= {2020: 1.0, 2021: 1.13, 2022: 1.23, 2023: 1.16, 2024: 1.03}[year]
                if degree == 'Research Doctorate' and season == 'Fall':
                    annual *= {2020: 1.14, 2021: 1.0, 2022: .91, 2023: 1.0, 2024: 1.12}[year]
                n = int(rng.integers(cfg['count'] - 12, cfg['count'] + 13))
                mu = np.log(cfg['base'] * seasonal * annual) - cfg['sigma']**2 / 2
                vals = rng.lognormal(mu, cfg['sigma'], size=n)
                for v in vals:
                    rows.append({'Completed.Term.Descr': f'{season} {year}',
                                 'Degree.Descr': degree,
                                 'Completed.Time': round(float(v), 3)})
    return pd.DataFrame(rows).sample(frac=1, random_state=seed).reset_index(drop=True)


if __name__ == '__main__':
    dest = Path(__file__).resolve().parent / 'synthetic_completion_data.csv'
    df = generate()
    df.to_csv(dest, index=False)
    print(f'Generated {len(df):,} fictional records: {dest}')
