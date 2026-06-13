"""
baseline_model.py
Baseline linear regression model for NCHS birthweight prediction.
Requires real NCHS natality .dat files mounted at /app/data/
"""

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ── Field specifications from NCHS 1969-1971 codebook ─────────
FIELD_SPECS = {
    'data_year':          (0,  1),
    'resident_status':    (11, 12),
    'res_state':          (12, 14),
    'occ_state':          (27, 29),
    'sex_child':          (34, 35),
    'race_child_recode3': (39, 40),
    'mat_age_recode8':    (48, 49),
    'gestation_recode10': (94, 96),
    'birthweight_grams':  (72, 76),
    'plurality_recode2':  (82, 83),
    'mat_edu_recode6':    (101, 102),
    'birth_order_recode9':(62, 63),
}

FEATURES = [
    'mat_age_recode8',
    'mat_edu_recode6',
    'race_child_recode3',
    'plurality_recode2',
    'sex_child',
    'gestation_recode10'
]
OUTCOME = 'birthweight_grams'

# Missing/special codes to exclude per NCHS codebook
MISSING_CODES = {
    'birthweight_grams':  [9999],
    'mat_age_recode8':    [9],
    'mat_edu_recode6':    [0],
    'race_child_recode3': [9],
    'gestation_recode10': [0, 10],
}


def load_nchs_dat(filepath: str) -> pd.DataFrame:
    """
    Parse a fixed-width NCHS natality .dat file.
    Field positions follow the 1969-1971 codebook (1-indexed
    in documentation; converted to 0-indexed slices here).
    """
    records = []
    with open(filepath, 'r', errors='replace') as f:
        for line in f:
            line = line.rstrip('\r\n')
            if len(line) < 215:
                continue
            record = {
                field: line[start:end].strip()
                for field, (start, end) in FIELD_SPECS.items()
            }
            records.append(record)

    df = pd.DataFrame(records)

    # Convert to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply NCHS codebook exclusion rules."""
    for col, codes in MISSING_CODES.items():
        if col in df.columns:
            df = df[~df[col].isin(codes)]
    df = df.dropna(subset=FEATURES + [OUTCOME])
    return df


def build_pipeline() -> Pipeline:
    """Construct the baseline sklearn Pipeline."""
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model',  LinearRegression())
    ])


def evaluate(pipeline, X_test, y_test):
    """Return test RMSE and R²."""
    y_pred = pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)
    return rmse, r2


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python baseline_model.py <path_to_dat_file>")
        sys.exit(1)

    df  = load_nchs_dat(sys.argv[1])
    df  = clean_data(df)
    X   = df[FEATURES]
    y   = df[OUTCOME]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    rmse, r2 = evaluate(pipeline, X_test, y_test)

    print(f"Test RMSE : {rmse:.1f} grams")
    print(f"Test R²   : {r2:.4f}")