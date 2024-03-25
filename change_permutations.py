# Given an amount of money and a sorted list of coin denominations, output the number of ways to
# make the amount out of those denominations.
from typing import List


def main():
    print(count_permutations_bottom_up(4, [1, 2, 3]))


def count_permutations_recursive(amount: int, denominations: List[int], current_index=0) -> int:
    # Recursive approach, where the top-level method will try adding each coin and calling the method for the
    # new value.
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if current_index == len(denominations):
        return 0

    current_coin = denominations[current_index]

    possibilities = 0
    while amount >= 0:
        possibilities += count_permutations_recursive(amount, denominations, current_index+1)
        amount -= current_coin

    return possibilities


def count_permutations_bottom_up(amount: int, denominations: List[int]) -> int:
    # bottom-up approach, where the number of ways of getting each possible value are calculated as we iterate through
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]


if __name__ == '__main__':
    main()
