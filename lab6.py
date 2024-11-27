'''
Created on 10/23/2024
@author: Yahia Abdelsalam
Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
CS115 - Lab 6
'''

# Check if the number is odd by using the modulus operator.
# Returns True if n is odd, False if n is even.
def isOdd(n):
    '''
    Returns whether or not the integer argument is odd.
    
    Explanation:
    - For odd numbers in base-10, the least-significant bit in base-2 is 1.
    - For even numbers in base-10, the least-significant bit in base-2 is 0.
    This is because odd numbers cannot be divided by 2 without a remainder, 
    which manifests as a 1 in the rightmost position in binary.
    '''
    return n % 2 != 0


# Convert a non-negative integer n to its binary representation as a string.
# If n is 0, return an empty string.
def numToBinary(n):
    '''
    Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.

    Additional Explanation:
    - When converting from base-10 to base-2, we find the largest power of 2 
      that fits into the number, subtract it, and continue with the remainder.
    '''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1'
    else:
        return numToBinary(n // 2) + '0'


# Convert a string s of 0 and 1 to its decimal representation.
# An empty string represents 0.
def binaryToNum(s):
    '''
    Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.

    Explanation:
    - Removing the least-significant bit (rightmost digit) in a binary number 
      effectively divides the number by 2 (discarding the remainder).
    '''
    if s == '':
        return 0
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])


# Increment an 8-bit binary string s by 1.
def increment(s):
    '''
    Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.

    Explanation:
    - This function ensures the result remains 8 bits long by using modulus 256.
    '''
    new_num = (binaryToNum(s) + 1) % 256
    return (8 * '0' + numToBinary(new_num))[-8:]


# Count up from an 8-bit binary string, printing a total of n+1 binary strings.
def count(s, n):
    '''
    Precondition: s is a string of 8 bits.
    Prints the binary representation of s incremented n times.
    '''
    if n < 0:
        return
    print(s)
    if n > 0:
        count(increment(s), n - 1)


# Convert a non-negative integer n to its ternary representation as a string.
# If n is 0, return an empty string.
def numToTernary(n):
    '''
    Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer n.
    If n is 0, the empty string is returned.

    Explanation:
    - Ternary representation uses base 3, with digits 0, 1, and 2.
    '''
    if n == 0:
        return ''
    else:
        return numToTernary(n // 3) + str(n % 3)


# Convert a string of 0s, 1s, and 2s (ternary) to its decimal representation.
def ternaryToNum(s):
    '''
    Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.
    '''
    if s == '':
        return 0
    else:
        return 3 * ternaryToNum(s[:-1]) + int(s[-1])
