# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python**, **Machine Learning**, and **Streamlit**. The application recommends five similar movies based on the selected movie using cosine similarity and displays their posters using the TMDB API.

---

## 🚀 Features

- Content-based movie recommendations
- Recommends the top 5 similar movies
- Interactive Streamlit web interface
- Fast similarity search using cosine similarity
- Simple and user-friendly interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- TMDB API

---

## 📂 Dataset

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 📊 Machine Learning Workflow

1. Load movie and credits datasets
2. Merge both datasets
3. Data preprocessing
4. Feature engineering
5. Create a combined **tags** column
6. Text vectorization using CountVectorizer
7. Compute cosine similarity
8. Save processed data using Pickle
9. Build a Streamlit web application

---

## 📁 Project Structure

```
Movie_Recommendation_System/
│
├── app.py
├── recommend_movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Move into the project directory

```bash
cd <repository-name>
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

- Select a movie from the dropdown
- Click **Recommend**
- View five similar movie recommendations
- Display corresponding movie posters

---

## 📦 Libraries Used

- pandas
- numpy
- scikit-learn
- streamlit
- requests
- pickle

---

## 🔮 Future Improvements

- Search bar with autocomplete
- Genre-based filtering
- Movie ratings and overview
- Cast and crew information
- Trailer integration
- User authentication
- Hybrid recommendation system

---

## 👩‍💻 Author

**Manjari M Varma**

LinkedIn: https://www.linkedin.com/in/<your-linkedin-id>/

GitHub: https://github.com/manjari-varma05

---

