import streamlit as st
import pickle
import requests


# ---------------- Load Pickle Files ---------------- #
movies = pickle.load(open('recommend_movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_titles = movies['title'].values

# ---------------- Streamlit UI ---------------- #
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a Movie",
    movie_titles
)

# ---------------- Recommendation Function ---------------- #
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

# ---------------- Button ---------------- #
if st.button("Recommend"):

    names = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        

    with col2:
        st.text(names[1])
        

    with col3:
        st.text(names[2])
        

    with col4:
        st.text(names[3])
        

    with col5:
        st.text(names[4])
        