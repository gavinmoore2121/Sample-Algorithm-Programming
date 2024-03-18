# Given a list of ints representing stock prices, print the max profit possible to earn
# in one buy and sale.
from typing import List


def main():
    print(calc_max_profit([10, 7, 5, 8, 11, 9]))  # Expect 6 profit
    print(calc_max_profit([10, 9, 8, 7, 6]))  # Expect -1 profit


def calc_max_profit(stock_prices: List[int]):
    # Use greedy approach: iterate through and check if selling on each day
    # would be more profitable than selling on the prior day.
    # Track max profit, and min buy price at each time.
    # Time complexity: O(n). Space complexity: O(1).

    # Pre-filling this value allows the algorithm to also calc the minimum loss, if the price
    # rose at each time.
    current_max_profit = stock_prices[1] - stock_prices[0]
    current_min_buy = min(stock_prices[0], stock_prices[1])

    for i in range(2, len(stock_prices)):
        if current_max_profit < stock_prices[i] - current_min_buy:
            current_max_profit = stock_prices[i] - current_min_buy
        if current_min_buy > stock_prices[i]:
            current_min_buy = stock_prices[i]

    return current_max_profit


if __name__ == '__main__':
    main()
