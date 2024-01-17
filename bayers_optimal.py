import numpy as np

# Probabilities of each classifier given D
Pr_h1_D = 0.4
Pr_h2_D = 0.2
Pr_h3_D = 0.4

# Probabilities of each test instance being classified as "+" by each classifier
Pr_h1_o1_plus = 0.5
Pr_h2_o1_plus = 0.6
Pr_h3_o1_plus = 0.3

Pr_h1_o2_plus = 0.2
Pr_h2_o2_plus = 0.9
Pr_h3_o2_plus = 0.7

Pr_h1_o3_plus = 0.3
Pr_h2_o3_plus = 0.0
Pr_h3_o3_plus = 0.4

# Probabilities of each test instance being classified as "-" by each classifier
Pr_h1_o1_minus = 0.5
Pr_h2_o1_minus = 0.4
Pr_h3_o1_minus = 0.7

Pr_h1_o2_minus = 0.8
Pr_h2_o2_minus = 0.1
Pr_h3_o2_minus = 0.3

Pr_h1_o3_minus = 0.7
Pr_h2_o3_minus = 1.0
Pr_h3_o3_minus = 0.6

# Bayes optimal classifier calculates the combined probability
# Pr(+|D) = Σ ( Pr(+|hi) * Pr(hi|D) ) for all i classifiers
# Similarly for Pr(-|D)

Pr_o1_plus_Bayes_optimal = (Pr_h1_o1_plus * Pr_h1_D) + (Pr_h2_o1_plus * Pr_h2_D) + (Pr_h3_o1_plus * Pr_h3_D)
Pr_o1_minus_Bayes_optimal = (Pr_h1_o1_minus * Pr_h1_D) + (Pr_h2_o1_minus * Pr_h2_D) + (Pr_h3_o1_minus * Pr_h3_D)

Pr_o2_plus_Bayes_optimal = (Pr_h1_o2_plus * Pr_h1_D) + (Pr_h2_o2_plus * Pr_h2_D) + (Pr_h3_o2_plus * Pr_h3_D)
Pr_o2_minus_Bayes_optimal = (Pr_h1_o2_minus * Pr_h1_D) + (Pr_h2_o2_minus * Pr_h2_D) + (Pr_h3_o2_minus * Pr_h3_D)

Pr_o3_plus_Bayes_optimal = (Pr_h1_o3_plus * Pr_h1_D) + (Pr_h2_o3_plus * Pr_h2_D) + (Pr_h3_o3_plus * Pr_h3_D)
Pr_o3_minus_Bayes_optimal = (Pr_h1_o3_minus * Pr_h1_D) + (Pr_h2_o3_minus * Pr_h2_D) + (Pr_h3_o3_minus * Pr_h3_D)

# Results
results = {
    "Pr[o1+|Bayes optimal]": Pr_o1_plus_Bayes_optimal,
    "Pr[o1-|Bayes optimal]": Pr_o1_minus_Bayes_optimal,
    "Pr[o2+|Bayes optimal]": Pr_o2_plus_Bayes_optimal,
    "Pr[o2-|Bayes optimal]": Pr_o2_minus_Bayes_optimal,
    "Pr[o3+|Bayes optimal]": Pr_o3_plus_Bayes_optimal,
    "Pr[o3-|Bayes optimal]": Pr_o3_minus_Bayes_optimal,
}

# Printing results with better readability
for key, value in results.items():
    print(f"{key}: {value:.2f}")
