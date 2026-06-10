from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # allow frontend to call this API

# Load trained model once at startup
MODEL_PATH = os.path.join(
    os.path.dirname(__file__), 'models', 'model.pkl')
model = joblib.load(MODEL_PATH)
print("✓ Model loaded successfully")

# Encoding maps — must match train.py exactly
FUEL_MAP     = {'Petrol':0,'Diesel':1,'CNG':2,'LPG':3,'Electric':4}
SELLER_MAP   = {'Individual':0,'Dealer':1,'Trustmark Dealer':2}
TRANS_MAP    = {'Manual':0,'Automatic':1}
OWNER_MAP    = {'First Owner':0,'Second Owner':1,
               'Third Owner':2,'Fourth & Above Owner':3}

@app.route('/')
def home():
    return jsonify({'status': 'CarValue API running'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validate required fields
        required = ['year','km_driven','fuel',
                    'seller_type','transmission','owner']
        for field in required:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Encode text inputs to numbers
        fuel   = FUEL_MAP.get(data['fuel'], 0)
        seller = SELLER_MAP.get(data['seller_type'], 0)
        trans  = TRANS_MAP.get(data['transmission'], 0)
        owner  = OWNER_MAP.get(data['owner'], 0)

        features = np.array([[
            int(data['year']),
            int(data['km_driven']),
            fuel, seller, trans, owner
        ]])

        price = model.predict(features)[0]

        return jsonify({
            'predicted_price' : round(float(price), 2),
            'price_lakh'      : round(float(price) / 100000, 2),
            'range_low'       : round(float(price) * 0.88 / 100000, 2),
            'range_high'      : round(float(price) * 1.12 / 100000, 2),
            'status'          : 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)