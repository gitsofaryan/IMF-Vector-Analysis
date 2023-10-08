from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)


def analyze_imf_data(df):
    # Implement your analysis logic here
    # You can use Pandas and NumPy for data manipulation and analysis

    # Example: Calculate mean Bx, By, and Bz values
    mean_bx = df['Bx'].mean()
    mean_by = df['By'].mean()
    mean_bz = df['Bz'].mean()

    # Example: Detect reconnection events
    reconnection_events = detect_reconnection(df)  # Implement this function

    analysis_result = f"Mean Bx: {mean_bx:.2f}, Mean By: {mean_by:.2f}, Mean Bz: {mean_bz:.2f}\n"
    analysis_result += f"Reconnection Events: {', '.join(reconnection_events)}"  # Format the events

    return analysis_result

def detect_reconnection(df):
    threshold = 1.0  # Adjust this threshold based on your data and criteria
    reconnection_events = []

    for i in range(1, len(df)):
        # Detect a significant change in Bx
        if abs(df['Bx'].iloc[i] - df['Bx'].iloc[i - 1]) > threshold:
            reconnection_events.append(df['Timestamp'].iloc[i])

    return reconnection_events




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            df = pd.read_csv(uploaded_file)
            result = analyze_imf_data(df)  # Implement your analysis function
            return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
