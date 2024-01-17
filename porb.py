from collections import defaultdict

def calculate_probability_distribution(operation, prob_X, prob_Y):
    prob_Z = defaultdict(float)
    for x in prob_X:
        for y in prob_Y:
            if operation == 'add':
                z = x + y
            elif operation == 'multiply':
                z = x * y
            prob_Z[z] += prob_X[x] * prob_Y[y]
    return prob_Z

# Probabilities for X and Y
prob_X = {k: 1/4 for k in range(1, 5)}
prob_Y = {k: 1/3 for k in range(1, 4)}

# Ask the user to choose the operation
print("Choose the operation for calculating the probability distribution of Z:")
print("Type 'add' for Z = X + Y")
print("Type 'multiply' for Z = X * Y")
operation = input("Enter your choice (add/multiply): ").strip().lower()

# Validate user input
while operation not in ['add', 'multiply']:
    print("Invalid choice. Please type 'add' for addition or 'multiply' for multiplication.")
    operation = input("Enter your choice (add/multiply): ").strip().lower()

# Calculate the probability distribution for Z based on the user's choice
prob_Z = calculate_probability_distribution(operation, prob_X, prob_Y)

# Print out the probabilities for all z values
print(f"\nProbabilities for Z = X { 'plus' if operation == 'add' else 'multiplied by' } Y:")
for z in sorted(prob_Z):
    print(f"Pr[Z = {z}] = {prob_Z[z]:.5f}")

