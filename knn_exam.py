import numpy as np

def manhattan_distance(point1, point2):
    return sum(abs(p1-p2) for p1, p2 in zip(point1, point2))

def euclidean_distance(point1, point2):
    return np.sqrt(sum((p1-p2)**2 for p1, p2 in zip(point1, point2)))

def knn_predict(query_point, labeled_points, k, distance_type='L1'):
    # Choose the distance function based on the distance type
    distance_fn = manhattan_distance if distance_type == 'L1' else euclidean_distance
    
    # Calculate the distance from the query point to each labeled point
    distances = [(distance_fn(query_point, point), label) for point, label in labeled_points]
    
    # Sort the distances
    sorted_distances = sorted(distances, key=lambda x: x[0])
    
    # Find the k-nearest neighbors
    k_nearest_neighbors = sorted_distances[:k]
    
    # Count the votes for each class
    class_votes = {}
    for _, label in k_nearest_neighbors:
        if label in class_votes:
            class_votes[label] += 1
        else:
            class_votes[label] = 1
    
    # Find the class with the most votes
    predicted_class = max(class_votes, key=class_votes.get)
    return predicted_class

# Example usage:
# Define your labeled points as (x, y, label), where label is 'circle' or 'square'
labeled_points = [
    ((2, 2), 'circle'), ((1, 8), 'circle'), ((2, 9), 'circle'), ((4, 9), 'circle'), 
    ((5, 6), 'circle'), ((6, 7), 'circle'), ((9, 9), 'circle'),


    ((3, 3), 'square'), ((6, 1), 'square'), ((6, 2), 'square'), ((7, 3), 'square'), ((8, 3), 'square'),
    ((7, 4), 'square'), ((8, 4), 'square')
    # Add more points as needed
]

# Define your query point
query_point = (6, 6)

# Predict class for different values of k using L1 norm (Manhattan)
for k in range(1, 8): # You can set the range of k as needed
    prediction = knn_predict(query_point, labeled_points, k, distance_type='L1')
    print(f"Prediction using L1 norm for k={k}: {prediction}")

# Predict class for different values of k using L2 norm (Euclidean)
for k in range(1, 8): # You can set the range of k as needed
    prediction = knn_predict(query_point, labeled_points, k, distance_type='L2')
    print(f"Prediction using L2 norm for k={k}: {prediction}")
