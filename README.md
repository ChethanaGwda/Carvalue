# 🚗 CarValue – AI Powered Used Car Price Prediction System

CarValue is a Machine Learning based web application that predicts the resale value of used cars using vehicle details such as manufacturing year, fuel type, transmission, ownership history, and kilometers driven.

The application also provides a seller dashboard, trending car insights, and an interactive user experience for both buyers and sellers.

---

## ✨ Features

### 👨‍💼 Buyer Module
- Predict used car market value instantly
- View fair price and good price range
- Detailed value factor analysis
- Interactive UI with real-time calculations

### 🚘 Seller Module
- Estimate optimal selling price
- Upload vehicle images
- Enter vehicle condition and ownership details
- Get recommended listing price range

### 📊 Analytics Dashboard
- Price prediction using Machine Learning
- Value factor breakdown
- Trending car sales information
- Market insights for buyers and sellers

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Random Forest Regressor
- Pandas
- NumPy

### Tools
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```text
CarValue/
│
├── backend/
│   ├── main.py
│   ├── train.py
│   └── models/
│       └── model.pkl
│
├── dataset/
│   └── cars.csv
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── images/
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/CarValue.git
cd CarValue
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
cd backend
python main.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

### Run Frontend

Open:

```text
frontend/index.html
```

or

```bash
cd frontend
python -m http.server 5500
```


---

## 📈 Machine Learning Model

The prediction model is trained using a Random Forest Regressor on historical used-car sales data.

Input Features:

- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Transmission
- Seller Type
- Ownership

Output:

- Predicted Market Value
- Fair Price Range
- Recommended Selling Price



## 🎯 Future Enhancements

- User Authentication
- Cloud Deployment
- Vehicle Image Analysis
- AI-based Price Recommendation
- Real-Time Market Data Integration
- Car Comparison Engine

