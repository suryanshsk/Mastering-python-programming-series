# Day 86: Building Neural Networks with Keras
# Make sure Keras is installed: pip install keras

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Step 1: Generate some sample data for binary classification
# Features: 10 input values per sample
# Labels: 0 or 1 (binary output)
np.random.seed(42)  # For reproducibility
X = np.random.rand(100, 10)  # 100 samples, 10 features each
y = np.random.randint(2, size=100)  # 100 labels (0 or 1)

# Step 2: Create a simple neural network
model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),  # First hidden layer
    Dense(16, activation='relu'),                    # Second hidden layer
    Dense(1, activation='sigmoid')                   # Output layer
])

# Step 3: Compile the model
# Binary classification requires binary_crossentropy as the loss function
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 4: Train the model
# Training for 10 epochs
model.fit(X, y, epochs=10, batch_size=8)

# Step 5: Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f"Model Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

# Step 6: Make predictions
sample_data = np.random.rand(5, 10)  # Generate 5 new samples
predictions = model.predict(sample_data)

print("\nPredictions:")
for i, pred in enumerate(predictions):
    print(f"Sample {i+1}: {pred[0]:.4f} (Probability of Class 1)")
