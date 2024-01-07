from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load the CSV data
    df = pd.read_csv("data.csv")
    
    # Convert the DataFrame to a list of dictionaries
    records = df.to_dict(orient='records')
    
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
