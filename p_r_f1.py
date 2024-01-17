from collections import defaultdict

# Sample data: a list of tuples with true class and predicted class
data = [
    ('A', 'A'),
    ('A', 'B'),
    ('A', 'A'),
    ('A', 'A'),
    ('A', 'B'),
    ('B', 'A'),
    ('B', 'B'),
    ('B', 'B'),
    ('B', 'B'),
    ('B', 'B'),

    # ... (add all your data here)
    # ('C', 'C') <- format for each entry
]

# Function to calculate precision, recall, and F1 score
def calculate_metrics(data):
    true_positive = defaultdict(int)
    false_positive = defaultdict(int)
    false_negative = defaultdict(int)
    
    # Calculate true positives, false positives, and false negatives
    for true_class, predicted_class in data:
        if true_class == predicted_class:
            true_positive[true_class] += 1
        else:
            false_positive[predicted_class] += 1
            false_negative[true_class] += 1

    # Calculate precision, recall, and F1 score for each class
    metrics = {}
    for class_label in set(true_positive.keys()).union(false_positive.keys()).union(false_negative.keys()):
        precision = true_positive[class_label] / (true_positive[class_label] + false_positive[class_label]) if class_label in true_positive else 0
        recall = true_positive[class_label] / (true_positive[class_label] + false_negative[class_label]) if class_label in true_positive else 0
        f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        metrics[class_label] = {
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score
        }

    return metrics

# Calculate metrics
metrics = calculate_metrics(data)

# Display the metrics for each class
for class_label, metric in metrics.items():
    print(f"Class {class_label}: Precision = {metric['precision']:.2f}, Recall = {metric['recall']:.2f}, F1 Score = {metric['f1_score']:.2f}")
