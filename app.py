from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import joblib

app = Flask(__name__)

# Load your trained pipeline
pipeline = joblib.load(r"notebooks/rfm_segmentation_pipeline.pkl")

# Cluster label mapping
cluster_labels = {
    0: 'Low Engagement',
    1: 'High Engagement',
    2: 'At-Risk',
    3: 'Medium Engagement'
}

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/segment', methods=['POST'])
def segment():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "Empty file name", 400

    try:
        df = pd.read_csv(file)

        # Check if required columns exist (including customer ID)
        required_cols = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            return f"Missing required columns: {missing_cols}", 400

        # Select RFM features only for prediction
        df_rfm = df[['Recency', 'Frequency', 'Monetary']]

        # Predict clusters
        clusters = pipeline.predict(df_rfm)
        df['Segment'] = [cluster_labels[c] for c in clusters]

        # Prepare dataframe with CustomerID & Segment for display
        result_df = df[['CustomerID', 'Segment']]

        # Generate HTML table with Bootstrap classes and centered text
        html_table = result_df.to_html(index=False, classes='table table-bordered table-striped text-center') 

        # Render results.html with the result_df as HTML table
        return render_template('results.html', tables=[result_df.to_html(index=False, classes='table table-striped')])

    except Exception as e:
        return f"Error processing file: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
