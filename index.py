python
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
def load_data():
    data = pd.read_excel('Distribution of Pensioners 2022.xlsx')
    return data

data = load_data()

@app.route('/pensioners/quarter', methods=['GET'])
def get_pensioners_by_quarter():
    quarter = request.args.get('quarter')
    if quarter not in ['Q1', 'Q2', 'Q3', 'Q4']:
        return jsonify({'error': 'Invalid quarter. Choose from Q1, Q2, Q3, Q4.'}), 400
    
    filtered_data = data[data['Quarter'] == quarter]
    response = filtered_data.to_dict(orient='records')
    return jsonify(response)

@app.route('/pensioners/gender', methods=['GET'])
def get_pensioners_by_gender():
    gender = request.args.get('gender')
    if gender not in ['Male', 'Female']:
        return jsonify({'error': 'Invalid gender. Choose Male or Female.'}), 400

    filtered_data = data[data['Gender'] == gender]
    response = filtered_data.groupby('Quarter').sum()['Count'].to_dict()
    return jsonify(response)

@app.route('/pensioners/total', methods=['GET'])
def get_total_pensioners():
    total_pensioners = data['Count'].sum()
    return jsonify({'total_pensioners': total_pensioners})

if __name__ == '__main__':
    app.run(debug=True)
