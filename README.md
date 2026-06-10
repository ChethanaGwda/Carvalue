#  CarValue – Car Price Prediction System

CarValue is a Machine Learning based web application that predicts the resale value of used cars using vehicle details such as manufacturing year, fuel type, transmission, ownership history, and kilometers driven.

The application provides secure user authentication, a buyer and seller dashboard, trending car insights, and an interactive experience for users looking to buy, sell, or evaluate vehicles.

---

## ✨ Features

### 🔐 Authentication Module
- Secure login page with Google Sign-In interface
- User-friendly onboarding experience
- Protected access to CarValue dashboard
- Smooth authentication workflow before accessing the platform

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

### 🚗 Trending Cars Section
- Top-selling cars in the market
- Vehicle specifications and highlights
- Monthly sales insights
- Market trend visualization

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

### Authentication
- Google Sign-In UI
- Session-Based Navigation

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
│   ├── auth.html
│   ├── index.html
│   ├── style.css
│   └── images/
│
├── requirements.txt
└── README.md
```

---


## 🔄 Application Workflow

1. User opens the Authentication Page.
2. User clicks Continue with Google.
3. User is redirected to the CarValue Dashboard.
4. Buyer or Seller selects their preferred module.
5. Machine Learning model analyzes vehicle details.
6. Predicted market value and insights are displayed instantly.

---

## 📈 Machine Learning Model

The prediction model is trained using a Random Forest Regressor on historical used-car sales data.

### Input Features

- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Transmission
- Seller Type
- Ownership

### Output

- Predicted Market Value
- Fair Price Range
- Recommended Selling Price
- Value Factor Analysis



---

useful, consider giving it a star.
