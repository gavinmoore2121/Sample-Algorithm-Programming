# Goldbach's Conjecture
# @Author: Gavin Moore
# 3/4/2021
# v1.0

# Description: Given between 1 and 100 integers even integers between 4 and 32,000, determine the number of ways
# they can be represented as sums of two prime numbers. Output the number of representations, and each representation.
# Problem obtained from https://open.kattis.com/problems/goldbach2
#
# Expected input format:
#   n
#   x1
#   x2
#   ....
#   xn
#
# Sample input:
# 3
# 4
# 26
# 100
#
# Sample output:
# 4 has 1 representation(s)
# 2+2
#
# 26 has 3 representation(s)
# 3+23
# 7+19
# 13+13
#
# 100 has 6 representation(s)
# 3+97
# 11+89
# 17+83
# 29+71
# 41+59
# 47+53
#
# Methodology:
#   - Get input
#   - Find all prime numbers between 1 and x - 1, where x is the highest input value.
#   - Store these in both a list and a set.
#   - For each element y in the list, check if x - y is in the set. If it is, store x and y in a solutions list.
#
# Time efficiency: ~O( (n^(3/2) / log(n) )

import math
import sys
from time import perf_counter
from typing import List


def main():
    # Get input
    nums = get_user_input()
    start_time = perf_counter()

    # Create a iterable list of prime numbers
    prime_list = sieve_of_atkin(max(nums))

    # Create a set of prime numbers
    set_primes = set(prime_list)

    # Find and print solutions
    for num in nums:
        solutions = find_goldbachs_solutions(num, prime_list, set_primes)
        print_solution(num, solutions)

    print("Time: " + str(perf_counter() - start_time))


def print_solution(num, solutions):
    """
    Prints the solution in the proper format.

    :param num: The number that has been solved.
    :param solutions: A list containing the valid representations in pairs.
    on the remaining lines.
    """
    num_solutions = len(solutions)
    print(str(num) + " has " + str(num_solutions) + " representation(s)")
    for solution in solutions:
        print(solution)
    print()


def get_user_input() -> List[int]:
    """
    Return a list of user input.

    Separates user input into values based on the format 'num_to_read \n num \n num'. Returns a list containing the
    numbers to read.

    :return: A list of categorized user input.
    """
    lines_to_read = get_ints()
    nums = [get_ints()[0] for x in range(0, lines_to_read[0])]
    return nums


def get_ints() -> List[int]:
    """
    Parse an input line into integers.

    Divides a single string of whitespace-separated user-input integers from stdin into individual integers and
    saves them as a list.

    :return: A list of integers from user input.
    """
    return list(map(int, sys.stdin.readline().strip().split()))


def sieve_of_atkin(limit):
    """
    Generate all prime numbers up to limit.

    Runs the Sieve of Atkin, which detects prime numbers based on their result in modulus 60.
    :return: A list of prime numbers.
    """
    primes = []
    # Initialize 2 and 3 as primes.
    if limit > 2:
        primes.append(2)
    if limit > 3:
        primes.append(3)

    # Initialize a sieve, filled with False values
    sieve = [False] * (limit + 1)

    # Add a value to candidate primes if one of the following is true:
    #   a) n = (4*x*x) + (y*y) has an odd number of solutions and n % 12 = 1 or 5.
    #   b) n = (3*x*x) + (y*y) has an odd number of solutions and n % 12 = 7.
    #   c) n = (3*x*x) - (y*y) has an odd number of solutions where x > y and n % 12 = 11

    root_limit = math.ceil(math.sqrt(limit))
    for x in range(1, root_limit):
        for y in range(1, root_limit):
            # Toggle condition a
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            # Toggle condition b
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            # Toggle condition c
            if x > y:
                n = (3 * x * x) - (y * y)
                if n <= limit and n % 12 == 11:
                    sieve[n] ^= True

    # Remove multiples of squared primes
    for n in range(5, root_limit + 1):
        if sieve[n]:
            x = 1
            while x * n * n <= limit:
                sieve[x*n*n] = False
                x += 1

    # Fill into list
    for prime in range(5, limit):
        if sieve[prime]:
            primes.append(prime)

    return primes


def find_goldbachs_solutions(num, list_of_primes, set_of_primes) -> List[str]:
    """
    Given an even number, a list of prime numbers below the number, and a set of the same primes, find all Golbach's
    solutions for the number such that prime+prime = number. Maintain a list of solutions.

    :param num: The number to find solutions for.
    :param list_of_primes: A list of prime numbers below the target number.
    :param set_of_primes: A set of prime numbers below the target number.
    :return: A list of strings containing the solutions, in the format "prime1+prime2"
    """
    solutions = []
    for prime in list_of_primes:
        if prime + prime > num:
            break
        elif (num - prime) in set_of_primes:
            solutions.append(str(prime) + '+' + str(num - prime))

    return solutions


main()

