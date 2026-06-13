"""
Baseline Linear Regression Model
NCHS Vital Statistics Natality Data, 1969-1971
"""

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ── 1. Load data ──────────────────────────────────────────────
# Replace with your actual data loading code
# df = pd.read_fwf('data/US1969.dat', ...)

# ── 2. Define features and outcome ───────────────────────────
FEATURES = [
    'mat_age_recode8',
    'mat_edu_recode6',
    'race_child_recode3',
    'plurality_recode2',
    'sex_child',
    'gestation_recode10'
]
OUTCOME = 'birthweight_grams'

# ── 3. Train/test split ───────────────────────────────────────
# X_train, X_test, y_train, y_test = train_test_split(
#     df[FEATURES], df[OUTCOME],
#     test_size=0.20, random_state=42
# )

# ── 4. Pipeline ───────────────────────────────────────────────
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

# ── 5. Fit and evaluate ───────────────────────────────────────
# pipeline.fit(X_train, y_train)
# y_pred = pipeline.predict(X_test)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# r2   = r2_score(y_test, y_pred)
# print(f"Test RMSE: {rmse:.1f} grams")
# print(f"Test R²:   {r2:.4f}")
