# Euler's Number Factorial Approximation
# @Author: Gavin Moore
# 3/4/2021
# v1.0

# Description: Given a real number integer n (0 <= n <= 10,000), approximate Euler's number based on it's factorial
# form, e ~= Summation (1/0!) + (1/1!) + ... + (1/n!). The approximation must be accurate to an absolute or relative
# error of at most 10^-12.
# Problem retrieved from https://open.kattis.com/problems/eulersnumber.
#
# Expected input format:
# n
#
# Sample input:
# 3
#
# Sample output:
# 2.6666666666666665
#
# Sample input 2:
# 15
#
# Sample output 2:
# 2.718281828458995
#
# Methodology:
#   - Get input
#   - Represent the factorial approximation as a fraction, where the numerator = n! + n-1! + ... + 1, and the
#          denominator = n!.
#   - Calculate n!, adding each n-x! to the numerator during each step.
#   - Divide the fraction and output the value.
#
# Time efficiency: O(n)

import math
import sys
from time import perf_counter
from typing import List


def main():
    num = get_ints()[0]
    print(str(approx_eulers_factorial(num)))


def get_ints() -> List[int]:
    """
    Parse an input line into integers.

    Divides a single string of whitespace-separated user-input integers from stdin into individual integers and
    saves them as a list.

    :return: A list of integers from user input.
    """
    return list(map(int, sys.stdin.readline().strip().split()))


def approx_eulers_factorial(n):
    """
    Approximate Euler's number based on it's factorial form.

    Error from true e < 1/(n!), except when n = 0. Truncation errors may occur at extreme values of n.

    :param n:
    :return:
    """
    numerator = 1
    denominator = 1

    for num in range(n, 0, -1):
        # Calculate e as a fraction, where the numerator = n! + n-1! + ... n-n! and the denominator = n!
        denominator = denominator * num
        numerator = numerator + denominator

    return numerator/denominator


main()
