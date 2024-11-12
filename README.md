# 📈 Nepse Stock Market Predictor

A web application built using **Streamlit** to predict stock market prices for the Nepali Stock Exchange (**NEPSE**). This app utilizes a **Multiple Linear Regression Model** to forecast stock prices based on historical data from NEPSE. The project was developed in 2020 with the goal of providing insights and predictions for the Nepali stock market.

![Streamlit App Screenshot](https://user-images.githubusercontent.com/yourusername/yourimage.png)

## 🚀 Features
- 📊 Predicts stock prices for NEPSE-listed companies using multiple linear regression.
- 📈 Provides data visualization with interactive charts for better insights.
- 🗂 Uses historical stock data from NEPSE.
- 🔄 Real-time data updates using NEPSE live API.
- 📉 Recommendations based on historical performance and trends.

## 📦 Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Libraries**: 
  - `pandas` for data manipulation
  - `scikit-learn` for machine learning
  - `requests` for API calls
  - `plotly` and `matplotlib` for data visualization

## 📂 Project Structure


#!/bin/bash

# Script to set up and run the Nepse Stock Market Predictor

echo "🔄 Starting the setup process..."

# Step 1: Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed. Please install it and try again."
    exit
else
    echo "✅ Python3 is installed."
fi

# Step 2: Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "❌ pip is not installed. Installing pip..."
    sudo apt update
    sudo apt install python3-pip -y
else
    echo "✅ pip is installed."
fi

# Step 3: Create a virtual environment (optional but recommended)
echo "🔧 Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 4: Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Check if Streamlit is installed
if ! command -v streamlit &> /dev/null
then
    echo "❌ Streamlit is not installed. Installing Streamlit..."
    pip install streamlit
else
    echo "✅ Streamlit is installed."
fi

# Step 6: Run the Streamlit app
echo "🚀 Launching the Nepse Stock Market Predictor..."
streamlit run app.py

echo "✅ Setup complete. The app is running!"
