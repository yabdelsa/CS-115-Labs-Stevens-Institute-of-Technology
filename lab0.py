############################################################
# Name: Yahia Abdelsalam
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#  
############################################################

def same(word):
    """
    Checks if the first and last letters are the same

    Returns bool: returns true if the first and last letters are the same, False otherwise
    """

    word = word.lower() # Changes the word to lowercase
    return word[0] == word[-1] #Compares the first and last letters

print(same("Level"))
print(same("Hanna"))
print(same("Yahia"))
print(same("Python"))

def consecutiveSum(x, y):
    """
    Finds the sum of consecutive integers between two numbers

    x(int): the starting number
    y(int): the ending number

    Returns:
    int: the sum of integers between x and y (both x and y excluded)
    """
    return sum(range(x + 1, y))

print(consecutiveSum(1,5))
print(consecutiveSum(3,8))
print(consecutiveSum(2,6))


