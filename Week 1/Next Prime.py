"""
Understand:
    Given a number, return the next smallest prime number
    prime = number is divisible by 1 and itself

    1. Will the input number always be positive?
    2. Is there guaranteed to be a solution?

    Test cases:
        1 -> 2
        3 -> 5
        14 -> 17
        0 -> 2
        -10 -> 2

Plan:
    Brute force approach:
        - starting at the input number, iterate over the numbers until a prime is found
        - to check if a number is prime, iterate over the numbers from 2 to n - 1 and mod them with the input number
        - if the mod is 0, the number is not prime
        - else the number is prime

        Analysis:
            - time complexity: O(n*m)
                - n = distance to the next prime starting from input number (input to input*2)
                - m = checking if a number is prime
            - space complexity: O(1)
"""

def nextPrime(input):
    if input < 2:
        return 2
    for i in range(input, input * 2):
        if isPrime(i):
            return i
    return None

def isPrime(input):
    for i in range(2, input):
        if input % i == 0:
            return False
    return True