#!/usr/bin/python3

"""
contains to functions collatz and distinct_numbers
"""

from typing import List


def collatz(n: int) -> List[int]:
    """
    You're given a positive integer n.
    Write an algorithm that does the following:
        - If n is even, the algorithm divides n by 2.
        This is the new value of n
        - If n is odd, the algorithm multiplies it by 3 and adds 1.
        This is the new value of n.
        - The algorithm repeats this until n == 1.

    Implement this algorithm in this function
    and return a list of all the intermediate values of n.
    For example, if n = 3,
    the sequence of values is: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    So, your function would return: [3, 10, 5, 16, 8, 4, 2, 1]
    """

    new_list: List[int] = []

    new_list.append(n)
    if n == 1:
        return new_list

    if ((n % 2) == 1):
        n = (n * 3) + 1
    else:
        n = n // 2
    return new_list + collatz(n)


def distinct_numbers(numbers: List[int]) -> int:
    """
    You are given a list of integers (the list could be empty),
    calculate the number of distinct/unique values in the list.

    E.g if numbers = [2, 3, 2, 2, 3],
    then the answer is 2 since there are only 2 unique numbers: 2 and 3.
    """
    list_length = len(numbers)
    unique_list: List[int] = []
    if list_length == 0:
        return 0

    for i in range(0, list_length):
        unique_number = 0
        for j in range(i):
            if (numbers[i] == numbers[j]):
                unique_number = 1
                break
        if unique_number == 0:
            unique_list.append(numbers[i])
    return len(unique_list)
