import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# Load MovieLens data
@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    return movies, ratings

movies, ratings = load_data()

# Build simple pivot for user-item matrix
user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating')

# Choose a user to simulate (hardcoded for demo)
SAMPLE_USER_ID = 1

# Helper: Recommend movies not yet rated by sample user
def recommend_movies(user_id, top_n=5):
    # Find movies user hasn't rated yet
    rated_movies = user_movie_matrix.loc[user_id].dropna().index
    unrated_movies = user_movie_matrix.columns.difference(rated_movies)
    
    # For collaborative filtering, find most similar users
    user_sim = cosine_similarity(user_movie_matrix.fillna(0))
    user_sim_df = pd.DataFrame(user_sim, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    similar_users = user_sim_df[user_id].sort_values(ascending=False)
    
    # Weighted average ratings by similar users for each unrated movie
    scores = {}
    for movie in unrated_movies:
        # Ratings of this movie by other users
        valid_users = user_movie_matrix[movie].dropna().index
        if len(valid_users) == 0:
            continue
        weight_sum = similar_users[valid_users].sum()
        if weight_sum == 0:
            continue
        weighted_score = (user_movie_matrix.loc[valid_users, movie] * similar_users[valid_users]).sum() / weight_sum
        scores[movie] = weighted_score
    top_movie_ids = sorted(scores, key=scores.get, reverse=True)[:top_n]
    return movies[movies['movieId'].isin(top_movie_ids)][['title']]

# Streamlit UI
st.title("Simple Movie Recommender")
st.write("This demo recommends movies for sample user **1** based on collaborative filtering.")

if st.button("Show Recommendations"):
    recs = recommend_movies(SAMPLE_USER_ID, 5)
    st.write("Recommended movies for you:")
    for title in recs['title']:
        st.write(f"- {title}")

if st.checkbox("Show all available movies"):
    st.dataframe(movies[['movieId', 'title']].head(20))

