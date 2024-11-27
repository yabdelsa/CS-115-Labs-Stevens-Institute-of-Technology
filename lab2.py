############################################################
# Name: Yahia Abdelsalam
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 2
#  
############################################################

def dot(L, K):
    if not L or not K:
        return 0 # If one of the lists is empty, return 0
    return L[0] * K[0] + dot(L[1:], K[1:])
"""
Takes two lists of numbers, L and L, and returns the sum of multiplying elements from each list.
"""
print(dot([5, 3], [6, 4]))

def explode(S):
    if S == "": # If the string is empty, return an empty list
        return []
    return [S[0]] + explode(S[1:]) # Take the first character and explode the rest
"""
Takes a string S and returns a list where each characters in the string is an item in the list
"""
print(explode("hello"))

def ind(e, L):
    if not L:
        return 0
    if L[0] == e:
        return 0
    return 1 + ind(e, L[1:])
"""
Finds the first index where element e is in the list or string L
If e is not found, if returns the lenght of L.
"""
print(ind(42, [55, 77, 42, 12]))


def removeAll(e, L):
    if not L:
        return []
    if L[0] == e:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])
"""
Takes a list L and returns a new list that has all items equal to e removed.
"""
print(removeAll(42, [55, 77, 42, 11, 34, 69])) 

def myFilter(f, L):
    if not L:
        return []
    if f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    return myFilter(f, L[1:])
"""
Takes a function f and a list L.
Returns a new list with only the itmes where f(item) is true
"""
def even (X):
    return X % 2 == 0
print(myFilter(even, [0, 1, 2, 3, 4, 5, 6]))

def deepReverse(L):
    if not L:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1])
"""
Takes a list L and returns the reverse of the list
"""
print(deepReverse([1, 2, 3, 4, 5, 6]))




























    
