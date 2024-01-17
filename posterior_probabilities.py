from sympy import symbols, solve, Eq

# Define the symbols for probabilities
a, b, Pr_a, Pr_b = symbols('a b Pr_a Pr_b')

# Define the symbols for the likelihoods
likelihood_a, likelihood_b = symbols('likelihood_a likelihood_b')

# Given prior probabilities - change these according to your exam question
Pr_theta_a = Pr_a  # P(θ = a)
Pr_theta_b = Pr_b  # P(θ = b)

# Given data set D - update this according to the given data set in your exam
X = [0, 1, 1]  # Example: D = {X1 = 0, X2 = 1, X3 = 1}

# Define the likelihood functions according to your exam question
# Replace these with the correct functions from your exam
Pr_X_given_theta_a = likelihood_a
Pr_X_given_theta_b = likelihood_b

# The probability that the random variable θ equals a given the data set D
# This is derived using Bayes' Theorem
Pr_theta_a_given_D = (Pr_X_given_theta_a * Pr_theta_a) / (Pr_X_given_theta_a * Pr_theta_a + Pr_X_given_theta_b * Pr_theta_b)

# The probability that the random variable θ equals b given the data set D
# This is derived using Bayes' Theorem
Pr_theta_b_given_D = (Pr_X_given_theta_b * Pr_theta_b) / (Pr_X_given_theta_a * Pr_theta_a + Pr_X_given_theta_b * Pr_theta_b)

# Solve the equations for Pr_a and Pr_b assuming they sum to 1
# This is to find the values of Pr_a and Pr_b that would make the above probabilities valid
solutions = solve((Eq(Pr_a + Pr_b, 1), Eq(Pr_theta_a_given_D, Pr_theta_b_given_D)), (Pr_a, Pr_b))

# Output the equations for manual verification and solutions for Pr_a and Pr_b
print(f"P(θ = a|D) equation: {Pr_theta_a_given_D}")
print(f"P(θ = b|D) equation: {Pr_theta_b_given_D}")
print(f"Solutions for Pr_a and Pr_b: {solutions}")

# To adapt this code for your exam:
# 1. Update the 'X' list with the actual data from your exam question.
# 2. Replace 'likelihood_a' and 'likelihood_b' with the actual likelihood expressions from your exam.
# 3. Change the 'Pr_a' and 'Pr_b' symbols to reflect the given prior probabilities in your exam question.
# 4. Run the script to compute the posterior probabilities.
