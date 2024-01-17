import numpy as np

# Manually input the confusion matrix data
confusion_matrix = np.array([
    [13, 3, 4],  # Predictions for Actual Class A
    [2, 14, 2],  # Predictions for Actual Class B
    [5, 1, 9]    # Predictions for Actual Class C
])

# True Positives (diagonal of the confusion matrix)
tp = np.diag(confusion_matrix)
# False Positives (column sum minus True Positives)
fp = confusion_matrix.sum(axis=0) - tp
# False Negatives (row sum minus True Positives)
fn = confusion_matrix.sum(axis=1) - tp
# True Negatives (sum of all values minus fp, fn, and tp for each class)
tn = confusion_matrix.sum() - (fp + fn + tp)

# Precision, Recall, and F1 Score for each class
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * (precision * recall) / (precision + recall)

# Overall Accuracy
accuracy = tp.sum() / confusion_matrix.sum()

# Statements
statements = {
    "The test accuracy of the classifier is higher than 70%": accuracy > 0.7,
    "The precision for Class C is greater than the recall for Class A": precision[2] > recall[0],
    "The precision for Class A is equal to the recall for Class A": precision[0] == recall[0],
    "The precision for Class B is less than 75%": precision[1] < 0.75,
    "The recall for Class B is greater than the recall for Class C": recall[1] > recall[2],
}

# Print the results
print(f"Confusion Matrix:\n{confusion_matrix}")
print(f"\nPrecision for each class: {precision}")
print(f"Recall for each class: {recall}")
print(f"F1 Score for each class: {f1_score}")
print(f"\nOverall Accuracy: {accuracy:.2f}")

# Evaluate statements
print("\nEvaluating statements:")
for statement, value in statements.items():
    print(f"{statement}: {'True' if value else 'False'}")
