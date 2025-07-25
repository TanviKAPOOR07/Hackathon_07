# Hackathon_07
# MovieMatch-AI
# MovieMatch – AI-Powered Movie Recommendation System

## Project Description

MovieMatch is an easy-to-use AI-driven movie recommendation platform that personalizes movie suggestions based on user preferences by analyzing collaborative filtering on movie ratings. It helps users discover films tailored to their unique tastes, reducing choice overload.

## Features

- Personalized movie recommendations based on user similarity
- Interactive and beginner-friendly Streamlit web interface
- Transparent access to movie and ratings datasets
- Powered by real-world MovieLens dataset

## Technology Stack

- Python
- Streamlit (web interface)
- pandas (data handling)
- scikit-learn (machine learning for similarity computation)
- numpy (numerical operations)

## How It Works

1. Loads movies and user ratings data from the MovieLens dataset.
2. Builds a user-item rating matrix to capture user preferences.
3. Computes user-user cosine similarity based on rating patterns.
4. Predicts ratings for movies a user hasn’t seen by weighting similar users’ ratings.
5. Provides top personalized movie recommendations via the Streamlit web app.

## Setup and Installation
1-) pip install pandas streamlit scikit-learn numpy

2-) Place `movies.csv` and `ratings.csv` from the [MovieLens dataset](https://grouplens.org/datasets/movielens/latest/) in the project folder.

3-) To start the app:
streamlit run recommendation_app.py

## Usage

1. Open the app in your web browser (usually `http://localhost:8501`).
2. Select a user profile from the dropdown menu.
3. Click the **Show Recommendations** button to get personalized movie suggestions.
4. Optionally explore the sample movie and rating data.

## Future Improvements

- Add functionality for live user ratings and feedback.
- Incorporate genre and popularity filters for refined recommendations.
- Explore content-based and hybrid recommendation algorithms.
- Implement user authentication and personalized sessions.
- Develop a mobile-friendly version or API endpoint.

## Credits

- Data: [MovieLens Dataset by GroupLens](https://grouplens.org/datasets/movielens/latest/)
- Libraries: pandas, Streamlit, scikit-learn, numpy



