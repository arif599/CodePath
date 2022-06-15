"""
Understand:
    Given an unsorted array of integers, we want to find the length of the longest 
    subsequence such that elements in the subsequence are consecutive integers. 
    The consecutive numbers can be in any order.

    1. Will the array always have at least 2 elements?
    2. What should we return if the array is empty?
    3. What is there are no subsequences?
    4. Will there be duplicates in the array?

    Test cases:
        Input: [36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42] 
        Output: 5 
        Note: [36, 35, 33, 34, 32] is the longest subsequence of consecutive elements.

        Input: [2] 
        Output: 1

        Input: [] 
        Output: 0

        Input: [3, 9, 50, 2, 8, 4, 1]
        Output: 4 
        Note: [3, 2, 4, 1] is the longest subsequence of consecutive elements.

        Input: [1, 5, 29, 4, 3, 2, 1] 
        Output: 5 
        Note: [1, 5, 4, 3, 2] is the longest subsequence of consecutive elements, 
        duplicates don't add to the count.

Match:
    - array problem
    - sorting 
    - set

Plan:
    Approach 1
        - sort the array
        - iterate over the array and find the longest subsequence
        - Time: (nlogn)
        - Space: (1)

    Approach 2
        - create a set from the list
        - iterate over the set and find the starting element of a subsequence
        - starting element is the element where element-1 is not in the set
        - start another loop to iterate over the set and find the end element of a subsequence
        - keep track of the longest subsequence and keep the max length
        - Time: (n)
        - Space: (n)

"""

def longestConsecutiveSubsequence(arr):
    if len(arr) == 0:
        return 0

    maxLength = 0
    arrSet = set(arr)
    for num in arr:
        if num-1 not in set:
            # start a new subsequence
            currLength = 1
            while num+currLength in arrSet:
                currLength += 1
            maxLength = max(maxLength, currLength)

    return maxLength    