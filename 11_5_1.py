from sklearn.metrics import confusion_matrix

# Step 1: Actual and Predicted values
actual = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # True labels
predicted = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]  # Predicted labels by the model

# Step 2: Generate the Confusion Matrix
cm = confusion_matrix(actual, predicted)

# Step 3: Print the Confusion Matrix
print("Confusion Matrix:")
print(cm)

# Step 4: Explain the Result
print("\nExplanation:")
print(f"True Negatives (TN): {cm[0][0]}")
print(f"False Positives (FP): {cm[0][1]}")
print(f"False Negatives (FN): {cm[1][0]}")
print(f"True Positives (TP): {cm[1][1]}")
