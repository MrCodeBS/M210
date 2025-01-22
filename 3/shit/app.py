from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

@app.route('/')
def home():
    return render_template('index.html')

def validate_symbol(symbol):
    # Common symbol corrections
    symbol_corrections = {
        'APPL': 'AAPL',
        'APPLE': 'AAPL',
        'GOOG': 'GOOGL',
        'FB': 'META',
    }
    
    # Convert to uppercase and check for known corrections
    symbol = symbol.upper()
    return symbol_corrections.get(symbol, symbol)

@app.route('/stock_data', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol', 'IBM')
    symbol = validate_symbol(symbol)
    
    # Parameters for API request
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        if "Error Message" in data:
            return jsonify({"error": "Invalid symbol or API error"}), 400
            
        # Extract the daily time series data
        time_series = data.get('Time Series (Daily)', {})
        
        # Format the data for frontend
        formatted_data = []
        for date, values in time_series.items():
            formatted_data.append({
                'date': date,
                'open': values['1. open'],
                'high': values['2. high'],
                'low': values['3. low'],
                'close': values['4. close'],
                'volume': values['5. volume']
            })
            
        return jsonify(formatted_data)
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/company_info', methods=['GET'])
def get_company_info():
    symbol = request.args.get('symbol', 'IBM')
    
    params = {
        'function': 'OVERVIEW',
        'symbol': symbol,
        'apikey': API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return jsonify(response.json())
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)