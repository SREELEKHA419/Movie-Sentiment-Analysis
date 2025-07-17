Movie Review Sentiment Analysis

A simple machine learning web application that predicts the sentiment of a movie review as **Positive** or **Negative**.  
Built using **Python**, **Flask**, and **scikit-learn**, this project demonstrates basic Natural Language Processing (NLP) techniques through a user-friendly web interface.

---

 Project Overview

This project uses a logistic regression model trained on a sample dataset of movie reviews. The input text is transformed using a `CountVectorizer`, and the app predicts the sentiment label based on the learned patterns.

---

 Features

- Binary sentiment classification (Positive / Negative)
- Web interface to input custom movie reviews
- Pre-trained ML model with vectorizer
- Emoji-based sentiment feedback

---

 Tech Stack

- Python
- Flask
- Scikit-learn
- Joblib
- HTML / CSS

---

Project Structure

movie-review-sentiment-analysis/
├── app.py # Flask backend
├── sentiment_model.pkl # Trained logistic regression model
├── vectorizer.pkl # CountVectorizer for text
├── templates/
│ ├── index.html # Input form
│ └── result.html # Output page
├── static/
│ └── style.css # Styling (optional)
├── sentiment_analysis.ipynb # Jupyter notebook to train model
├── requirements.txt # Python dependencies
└── README.md # Project description



---

 How to Run

1. Clone the Repository
   ```bash
  git clone https://github.com/SREELEKHA419/movie-review-sentiment-analysis.git
   cd movie-review-sentiment-analysis
2. Install Requirements

  pip install -r requirements.txt

3. Run the Flask App

   python app.py

4.Open in Browser

   http://127.0.0.1:5000/

 Example
Input:
"The movie was brilliant! Great story and acting."

Output:
Positive 😊

License
This project is licensed under the MIT License.
Feel free to use, share, or modify it with proper attribution.

Developed By
Sreelekha A S
B.Tech Computer Science and Engineering
B. S. Abdur Rahman Crescent Institute of Science and Technology, Chennai



