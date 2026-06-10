import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import joblib, os

# ── 1. Load data (tab-separated file) ────────────────
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
csv_path = os.path.join(BASE, 'dataset', 'cars.csv')
df = pd.read_csv(csv_path, sep='\t')   # ← fix: sep='\t'

print("Columns:", df.columns.tolist())
print(f"Rows   : {len(df)}")

# ── 2. Keep only needed columns ───────────────────────
df = df[['year','selling_price','km_driven',
         'fuel','seller_type','transmission','owner']].copy()
df = df.dropna()

# ── 3. Encode text → numbers ──────────────────────────
fuel_map   = {'Petrol':0,'Diesel':1,'CNG':2,'LPG':3,'Electric':4}
seller_map = {'Individual':0,'Dealer':1,'Trustmark Dealer':2}
trans_map  = {'Manual':0,'Automatic':1}
owner_map  = {'First Owner':0,'Second Owner':1,
              'Third Owner':2,'Fourth & Above Owner':3,'Test Drive Car':4}

df['fuel']         = df['fuel'].map(fuel_map)
df['seller_type']  = df['seller_type'].map(seller_map)
df['transmission'] = df['transmission'].map(trans_map)
df['owner']        = df['owner'].map(owner_map)
df = df.dropna()

print(f"Rows after cleaning: {len(df)}")

# ── 4. Features & target ──────────────────────────────
X = df[['year','km_driven','fuel','seller_type','transmission','owner']]
y = df['selling_price']

# ── 5. Train / test split ─────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# ── 6. Train ──────────────────────────────────────────
model = RandomForestRegressor(
    n_estimators=200, max_depth=15,
    random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# ── 7. Evaluate ───────────────────────────────────────
y_pred = model.predict(X_test)
print(f"R² Score : {r2_score(y_test, y_pred):.4f}")
print(f"MAE      : ₹{mean_absolute_error(y_test, y_pred):,.0f}")

# ── 8. Save ───────────────────────────────────────────
joblib.dump(model, 'model.pkl')
print("✓ model.pkl saved!")