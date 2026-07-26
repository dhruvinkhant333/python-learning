# Title: The Restock Priority Sorter
# Difficulty: Core
# Topics Used: Dictionaries, List Comprehensions, Lambda Functions
# Problem Statement: Given inventory data as a dictionary mapping product name to (current_stock, reorder_threshold), build a sorted list of products that are below their threshold, ordered by how urgently they need restocking (the ones furthest below threshold first).
# Input: {"Pens": (5, 20), "Notebooks": (40, 30), "Erasers": (2, 10)}
# Output: ["Pens", "Erasers"]
# Constraints: Products at or above threshold are excluded entirely. Ties can be broken alphabetically.
# Logic Trigger: Think about what single number best represents "urgency" for each item before you sort anything.

# ---------------------------------------------------------------------------- #
#                                First solution                                #
# ---------------------------------------------------------------------------- #

inventory = {
    "Pens": (5, 20),
    "Notebooks": (40, 30),
    "Erasers": (2, 10)
}

restock = sorted(
    [product for product,(stock,threshold) in inventory.items() if stock < threshold],
    key=lambda product: inventory[product][1] - inventory[product][0],
    reverse=True
)

print(restock)


# ---------------------------------------------------------------------------- #
#                                second solution                               #
# ---------------------------------------------------------------------------- #
inventory = {
    "Pens": (5, 20),
    "Notebooks": (40, 30),
    "Erasers": (2, 10)
}

restock = sorted(
    inventory.items(), 
    key=lambda item: (item[1][1] - item[1][0], item[0]),
    reverse=True
)

result =[
    product
    for product,(stock, threshold) in restock
    if stock < threshold
]

print(result)