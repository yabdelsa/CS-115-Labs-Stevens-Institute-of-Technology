############################################################
# Name: Yahia Abdelsalam
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 3
#  
############################################################

def change(amount, coins):
    """
    Finds the minimum number of coins needed to make up a given amount.
    Returns float('inf') if it's not possible.
    
    """
    if amount == 0:  # Base Case: No coins needed for 0
        return 0
    if not coins:  # Base Case: No solution if no coins left
        return float("inf")

    first_coin = coins[0]
    if first_coin <= amount:
        use_it = change(amount - first_coin, coins) + 1
    else:
        use_it = float("inf")  # Skip if coin is too large

    lose_it = change(amount, coins[1:])  # Try without first coin
    return min(use_it, lose_it)  # Choose the best option

# Example usage:
result = change(45, [2, 4, 16, 28, 64])
print(result)  





