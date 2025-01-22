import pandas as pd

def load_data(file_path):
    """Load the ratings dataset."""
    return pd.read_csv(file_path)

def preprocess_data(ratings):
    """Prepare the data for the recommendation system."""
    # Create a pivot table with users as rows and items as columns
    ratings_matrix = ratings.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
    return ratings_matrix

if __name__ == "__main__":
    ratings = load_data("data/ratings.csv")
    ratings_matrix = preprocess_data(ratings)
    print(ratings_matrix)
