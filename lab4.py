############################################################
# Name: Yahia Abdelsalam
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 4
############################################################

def knapsack(capacity, itemList):
    """Solves the knapsack problem by recursively determining the maximum value"""
    if capacity == 0 or len(itemList) == 0:
        """If the remaining capacity is 0 or there are no more items to consider, return a value of 0 and an empty list of items"""
        return [0, []]
    weight, value = itemList[0]
    without_item = knapsack(capacity, itemList[1:])

    if weight <= capacity:
        """Check if the current item's weight is less than or equal to the available capacity. If so, we can consider including it in the knapsack."""
        with_item = knapsack(capacity - weight, itemList[1:])
        with_item[0] = with_item[0] + value
        with_item[1] = [[weight, value]] + with_item[1]
    else:
        """If the item's weight exceeds the available capacity, we cannot take it"""
        with_item = [0, []]


    if with_item[0] > without_item[0]:
        return with_item
    else:
        return without_item

print(knapsack(6, [[1, 4], [5,150], [4, 180]]))
    
