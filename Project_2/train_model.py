from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from preprocessing import load_data, preprocess_data

def train_model(ratings_matrix):
    """Train the recommendation model using cosine similarity."""
    user_similarity = cosine_similarity(ratings_matrix)
    np.fill_diagonal(user_similarity, 0)
    return user_similarity

if __name__ == "__main__":
    ratings = load_data("data/ratings.csv")
    ratings_matrix = preprocess_data(ratings)
    user_similarity = train_model(ratings_matrix)
    
    # Save the user similarity matrix
    np.save("data/user_similarity.npy", user_similarity)
    print("Model trained and user similarity matrix saved.")
