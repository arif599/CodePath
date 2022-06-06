"""
Understand:
    Write a function that takes in two strings 
    and returns true if the second string is substring of the first, 
    and false otherwise.

    1. Do spaces count as substring?
    2. Will the second string ever be empty?
    3. Will the second string ever be longer than the first?
    4. Can elements of the string be both characters and numbers?

    Test cases:
        "hello", "ell" -> True
        "", "" -> True
        "hello", "helloworld" -> False

Match:
    - string problem
    - substring
    - sliding window

Plan:
    Brute force approach:
        - iterate over the first string until the first character of the second string is found
        - check the characters of the second string against the first string till the length of the second string is reached
    Analysis:
        - time complexity: O(n*m)
            - n = length of the first string
            - m = length of the second string
        - space complexity: O(1)

Optimization:
    - sliding window?

Review:
    - Runthrough of code using test case = "hello", "ell" -> True
"""

def substring(large_str, potential_substr):
    if len(potential_substr) < 1:
        return True
    for i in range(len(large_str)):
        large_str_idx, j = i, 0
        while j < len(potential_substr) and large_str_idx < len(large_str) and large_str[large_str_idx] == potential_substr[j]:
            j += 1
            large_str_idx += 1
        if j + 1 == len(potential_substr):
            return True
    return False
    