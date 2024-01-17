import numpy as np

# Define the distance measure function with the given matrix
def dist(x, y, A):
    diff = np.array(x) - np.array(y)
    return np.sqrt(diff.T @ A @ diff)

# Matrix A as given in the question
A = np.array([[3, 1],
              [0, 2]])

# Centroids for clusters 1 and 2
mu1 = np.array([0, 2])
mu2 = np.array([4, 7])

# Points given in the question
points = {
    "Point (2,5)": np.array([2, 5]),
    "Point (4,0)": np.array([4, 0]),
    "Point (3,4)": np.array([3, 4]),
    "Point (3,3)": np.array([3, 3]),
    "Point (4,4)": np.array([4, 4])
}

# Assign points to the closest centroid
assignments = {}
for point_name, point in points.items():
    distance_to_mu1 = dist(point, mu1, A)
    distance_to_mu2 = dist(point, mu2, A)
    assignments[point_name] = "Cluster 1" if distance_to_mu1 < distance_to_mu2 else "Cluster 2"

print(assignments)
