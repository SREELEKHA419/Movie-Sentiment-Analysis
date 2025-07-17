from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.cluster import KMeans
import pandas as pd
import os
from werkzeug.utils import secure_filename

nltk.download('vader_lexicon')

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    score = None
    user_review = ""
    cluster_labels = []
    uploaded_file = None

    if request.method == 'POST':
        # Sentiment part
        user_review = request.form.get('review', "")
        if user_review.strip():
            score = sia.polarity_scores(user_review)["compound"]
            if score > 0.05:
                sentiment = "Positive 😊"
            elif score < -0.05:
                sentiment = "Negative 😞"
            else:
                sentiment = "Neutral 😐"

        # Clustering part
        file = request.files.get('file')
        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            df = pd.read_csv(filepath)

            df_numeric = df.select_dtypes(include=['int64', 'float64'])
            if not df_numeric.empty:
                kmeans = KMeans(n_clusters=3, random_state=0)
                df_numeric['Cluster'] = kmeans.fit_predict(df_numeric)
                cluster_labels = df_numeric['Cluster'].tolist()
                uploaded_file = filename

    return render_template('index.html',
                           review=user_review,
                           sentiment=sentiment,
                           score=score,
                           labels=cluster_labels,
                           filename=uploaded_file)

if __name__ == '__main__':
    app.run(debug=True)
