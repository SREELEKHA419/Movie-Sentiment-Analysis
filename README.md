
# 🎬 Movie Review Sentiment Analysis App

This Flask-based web application uses Natural Language Processing (NLP) to analyze movie reviews and predict whether a review is **Positive** or **Negative**. Users can submit a review and instantly get a sentiment classification.

---

 Project Structure

```

movie-sentiment-analysis/
├── app.py                  # Flask backend to handle form and prediction
├── requirements.txt        # Required Python libraries
├── movie\_reviews.xlsx      # Sample dataset of labeled reviews
├── sample\_customer\_data.xlsx  # Optional user/customer data for segmentation
├── templates/              # HTML templates
│   ├── index.html          # Input form for movie review
│   └── result.html         # Displays predicted sentiment
├── static/                 # Optional CSS for styling
│   └── style.css
├── OUTPUTS/                # Optional outputs (e.g., logs or screenshots)
└── README.md               # Project documentation

````

---

## 🚀 How to Run the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/movie-sentiment-analysis.git
   cd movie-sentiment-analysis
````

2. Install required packages

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application

   ```bash
   python app.py
   ```

4. Visit the app in your browser

   ```
   http://localhost:5000
   ```

---

 Technologies Used

* Python
* Flask
* scikit-learn
* pandas
* HTML/CSS (Jinja2)
* NLP (CountVectorizer, Logistic Regression)

---
 Dataset Info

* `movie_reviews.xlsx`: Contains sample reviews and their associated sentiment.
* `sample_customer_data.xlsx`: Additional data for customer segmentation or review enrichment (optional).

---

 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

👩‍💻 Author

Sreelekha A S
B.Tech CSE | B.S. Abdur Rahman Crescent Institute of Science and Technology
[GitHub](https://github.com/SREELEKHA419)

---

```
