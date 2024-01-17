from itertools import product

# Define the possible values of X and Y
X_values = range(1, 7) # creates a range of values from 1 to 6 for X
Y_values = range(1, 9) # creates a range of values from 1 to 8 for Y (similarly, we use 9 to include 8).

# Calculate the probability distribution of Z = X + Y
Z_probs = {}

# Since X and Y are independent, the probability of any combination is the product of the two probabilities
for x, y in product(X_values, Y_values): # iterates over all combinations of values for X and Y.
    z = x + y  # The sum of the two values
    Z_probs[z] = Z_probs.get(z, 0) + (1/6) * (1/8)  # Update the probability of Z

# Calculate specific probabilities
Pr_Z_gt_5 = sum(prob for outcome, prob in Z_probs.items() if outcome > 5) # calculates the sum of probabilities for all Z values greater than 5
Pr_Z_eq_7 = Z_probs.get(7, 0) # gets the probability for Z being exactly 7
Pr_Z_eq_4 = Z_probs.get(4, 0) # gets the probability for Z being exactly 4
Pr_Z_lt_7 = sum(prob for outcome, prob in Z_probs.items() if outcome < 7) # calculates the sum of probabilities for all Z values less than 7

print(Pr_Z_gt_5, Pr_Z_eq_7, Pr_Z_eq_4, Pr_Z_lt_7)
