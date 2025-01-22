import numpy as np
import pandas as pd
from preprocessing import load_data, preprocess_data

def recommend_items(user_id, ratings_matrix, user_similarity, top_n=5):
    """Recommend items to a user based on similarity to other users."""
    user_idx = user_id - 1
    similar_users = np.argsort(-user_similarity[user_idx])[:top_n]
    
    similar_users_ratings = ratings_matrix.iloc[similar_users]
    recommended_items = similar_users_ratings.mean(axis=0).sort_values(ascending=False).index
    
    return recommended_items[:top_n]

if __name__ == "__main__":
    ratings = load_data("data/ratings.csv")
    ratings_matrix = preprocess_data(ratings)
    
    # Load the trained user similarity matrix
    user_similarity = np.load("data/user_similarity.npy")
    
    user_id = int(input("Enter user ID for recommendations: "))
    recommendations = recommend_items(user_id, ratings_matrix, user_similarity, top_n=5)
    
    print(f"Recommended items for user {user_id}: {list(recommendations)}")
