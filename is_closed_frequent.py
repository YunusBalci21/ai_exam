# Updated Python code to determine closed frequent itemsets with provided lattice information

def is_closed_frequent(itemset, all_itemsets, threshold):
    itemset_support = all_itemsets.get(itemset, 0)
    if itemset_support >= threshold:
        for superset in all_itemsets:
            if set(itemset).issubset(set(superset)) and set(itemset) != set(superset):
                if all_itemsets[superset] >= itemset_support:
                    return False
        return True
    else:
        return False

# Define the support threshold
sigma = 4

# Define the support counts for each itemset as provided in the image
lattice_from_image = {
    # Update these values based on the support counts given in your exam
    'AB': 4, 'AC': 3, 'AD': 6, 'AE': 5,
    'BC': 3, 'BD': 4, 'BE': 3, 'CD': 4, 'CE': 3, 'DE': 6,
    'ABC': 2, 'ABD': 4, 'ABE': 3, 'ACD': 3, 'ACE': 2, 'ADE': 5,
    'BCD': 2, 'BCE': 1, 'BDE': 3, 'CDE': 3, 'ABCD': 2, 'ABCE': 1,
    'ABDE': 3, 'ACDE': 2, 'BCDE': 1, 'ABCDE': 1
}

# Generate the results by checking each itemset in the lattice
results = {itemset: is_closed_frequent(itemset, lattice_from_image, sigma) for itemset in lattice_from_image}

# Filter out single itemsets and prepare a report of the results
report = {itemset: 'Closed frequent' if status else 'Not closed frequent'
          for itemset, status in results.items() if len(itemset) > 1}

# Output the report
for itemset, status in report.items():
    print(f"Itemset {itemset} is {status} at threshold σ = {sigma}.")
