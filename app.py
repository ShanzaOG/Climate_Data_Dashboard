#!/usr/bin/python3
# climate_dashboard/app.py
from flask import Flask, render_template

app = Flask(__name__)

# Sample climate data (replace with your actual data)
climate_data = [
    {"year": 2022, "temperature": 25.5, "precipitation": 800},
    {"year": 2023, "temperature": 26.0, "precipitation": 750},
    {"year": 2024, "temperature": 25.8, "precipitation": 820},
    # Add more data as needed
]

@app.route('/')
def index():
    return render_template('index.html', climate_data=climate_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

