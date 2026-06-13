"""
validate.py
Smoke test: confirms the container environment is working correctly.
Runs without any data files — safe to execute in CI or on first build.
"""

import sys
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def generate_synthetic_births(n=10000, seed=42):
    """
    Generate synthetic birth records mirroring the NCHS
    1969-1971 natality file structure for validation purposes.
    Field names and value ranges follow the codebook exactly.
    No real NCHS data is used here.
    """
    rng = np.random.default_rng(seed)

    data = pd.DataFrame({
        # Maternal age recode 8 (1=<15, ..., 8=45-49)
        'mat_age_recode8': rng.integers(1, 9, n),

        # Maternal education recode 6
        # (1=0-8yrs, 2=9-11yrs, 3=12yrs,
        #  4=13-15yrs, 5=16+yrs, 6=Not stated)
        'mat_edu_recode6': rng.integers(1, 7, n),

        # Race of child recode 3
        # (1=White, 2=Other, 3=Black)
        'race_child_recode3': rng.integers(1, 4, n),

        # Plurality recode 2
        # (1=Singleton, 2=Multiple)
        'plurality_recode2': rng.choice(
            [1, 2], n, p=[0.97, 0.03]
        ),

        # Sex of child (1=Male, 2=Female)
        'sex_child': rng.integers(1, 3, n),

        # Gestation recode 10
        # (0=Not applicable, 1=<20wks, ..., 10=Not stated)
        'gestation_recode10': rng.integers(1, 10, n),
    })

    # Simulate birthweight with known relationships
    # so we can verify model behavior is directionally correct
    birthweight = (
        3300                                          # intercept
        + (data['mat_age_recode8'] - 4) * 18         # age effect
        - (data['mat_age_recode8'] - 4) ** 2 * 8     # quadratic age
        + data['mat_edu_recode6'] * 40                # education effect
        - (data['race_child_recode3'] == 3) * 250     # race disparity
        - (data['plurality_recode2'] == 2) * 900      # plurality penalty
        + (data['sex_child'] == 1) * 120              # sex effect
        + data['gestation_recode10'] * 85             # gestation effect
        + rng.normal(0, 480, n)                       # residual noise
    )

    data['birthweight_grams'] = np.clip(birthweight, 227, 8165)
    return data


def run_baseline_model(df):
    """Fit baseline linear regression and report test metrics."""

    FEATURES = [
        'mat_age_recode8',
        'mat_edu_recode6',
        'race_child_recode3',
        'plurality_recode2',
        'sex_child',
        'gestation_recode10'
    ]
    OUTCOME = 'birthweight_grams'

    X = df[FEATURES]
    y = df[OUTCOME]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model',  LinearRegression())
    ])

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)

    return rmse, r2, pipeline


def main():
    print("=" * 55)
    print("  Birthweight Analysis — Container Validation")
    print("  NCHS Natality Data 1969-1971 | Template Project")
    print("=" * 55)

    # 1. Library versions
    print("\n[1] Environment check")
    print(f"    Python     : {sys.version.split()[0]}")
    print(f"    NumPy      : {np.__version__}")
    print(f"    Pandas     : {pd.__version__}")
    import sklearn
    print(f"    scikit-learn: {sklearn.__version__}")

    # 2. Synthetic data
    print("\n[2] Generating synthetic birth records...")
    df = generate_synthetic_births(n=10000)
    print(f"    Records generated : {len(df):,}")
    print(f"    Birthweight mean  : {df['birthweight_grams'].mean():.1f}g")
    print(f"    Birthweight SD    : {df['birthweight_grams'].std():.1f}g")
    print(f"    Low birthweight   : "
          f"{(df['birthweight_grams'] < 2500).mean()*100:.1f}%")

    # 3. Baseline model
    print("\n[3] Fitting baseline linear regression...")
    rmse, r2, pipeline = run_baseline_model(df)
    print(f"    Test RMSE : {rmse:.1f} grams")
    print(f"    Test R²   : {r2:.4f}")

    # 4. Assertions — fail loudly if something is wrong
    print("\n[4] Running assertions...")
    assert rmse < 600,  f"RMSE too high: {rmse:.1f}g"
    assert r2   > 0.25, f"R² too low: {r2:.4f}"
    assert len(df) == 10000, "Record count mismatch"
    print("    All assertions passed.")

    print("\n✓ Container validated successfully.")
    print("  Replace synthetic data with real NCHS .dat files")
    print("  by mounting your data/ directory at runtime:")
    print("  docker run -v /path/to/data:/app/data birthweight-analysis")
    print("=" * 55)


if __name__ == "__main__":
    main()