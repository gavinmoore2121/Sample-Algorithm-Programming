# Given an array of integers, return an array consisting of the products of all other integers,
# besides the one in the current index. Division is not allowed.
import math
from typing import List


def main():
    print(calc_product_of_all_other_indexes([1, 7, 3, 4]))


def calc_product_of_all_other_indexes(ints: List[int]):
    # Greedy approach: Each product is effectively the value of all ints before, and all
    # ints after the current index. We can iterate through the forward once and backwards once,
    # storing and re-using the product of all ints before/after the current index. 
    # Time complexity: O(n). Space complexity: O(1).
    output = [None] * len(ints)

    # For each int, find product of all integers before it. Store it in output list, AND keep
    # a running tally.
    product_of_prior_nums = 1
    for i in range(len(ints)):
        output[i] = product_of_prior_nums
        product_of_prior_nums *= ints[i]

    # Repeat prior process backwards, to get products of all numbers AFTER current index.
    product_of_subsequent_nums = 1
    for i in range(len(ints)-1, -1, -1):
        output[i] *= product_of_subsequent_nums
        product_of_subsequent_nums *= ints[i]

    return output


if __name__ == '__main__':
    main()
