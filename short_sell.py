# Short sell
# @author: Gavin Moore
# 2/12/2021
# v1.2

# Description: Given N days of known price and K price of holding per day, find the maximum
# dollars that can be made from short-selling 100 shares. Problem retrieved from Kattis.org's CMICH2021 Competition.
#
# Expected input format:
#   num_days interest_per_day
#   price_day_1 price_day_2.... price_day_n
#       where all values are integers.
#
# Methodology:
#       - Get input, separate into array of days and interest price.
#       - Using a nested loop, for each number n iterate through the values in the array past it i and record the
#               highest profit obtained from any values i less than itself.
#       - While iterating n, if a value i would result in a negative profit, skip numbers n and begin iterating from
#               the larger value forward using the same methodology as above.
#       - This results in one comparison per value given, and one additional comparison for any max value of a generic
#               slice [0, n].
#
# Time complexity: O(n).

import sys
import time
from typing import List


def main():
    """
    Main run location of the file.

    Retrieves input, calls the correct algorithm, and prints output. Records and outputs the processing time.
    """
    # Replace 'get_user_input()' with 'generate_random_data()' to enable random testing.
    num_days, interest, prices = get_user_input()
    start_time = time.time()
    print(find_profit(interest, prices))
    print("--- Time elapsed: %s seconds ---" % (time.time() - start_time))


def input_sample():
    integer1 = int(input())
    list_of_ints = list(map(int, input().split()))
    integer2 = int(input())

    list_of_10_lines_of_ints = [list(map(int, input().split())) for n in range(10)]


def get_user_input() -> (int, int, List[int]):
    """
    Return a list of user input.

    Separates user input into values based on the format 'num_days interest \n price_1 price_2... price_n'. Returns
    a list containing num_days, interest, and a list of each day's prices in index 0, 1, and 2 respectively.

    @return: A list of categorized user input.
    """
    line = get_ints()
    num_days = line[0]
    interest = line[1]
    prices = get_ints()
    return num_days, interest, prices


def get_ints() -> List[int]:
    """
    Parse an input line into integers.

    Divides a single string of whitespace-separated user-input integers from stdin into individual integers and
    saves them as a list.

    @return: A list of integers from user input.
    """
    return list(map(int, sys.stdin.readline().strip().split()))


def find_profit(interest: int, prices: List[int]) -> int:
    """
    Return the highest profit obtainable from the data values.

    Calculates the highest profit obtainable by short-selling 100 shares given the daily interest and prices. Iterates
    through the list of values, saving the highest profit from any values smaller. When a larger value is reached,
    begins iterating from that value forward.

    @param interest: Number representing daily interest per 100 shares.
    @param prices: List of numbers showing daily prices per 1 share.
    @return: Maximum profit obtainable over the period, or 0 if profit is impossible.
    """
    highest_profit = -1
    i = 0
    # Iterate through the list of values until the end is reached.
    while i < len(prices):
        # The price, including interest, of 100 shares.
        biased_short_price = prices[i] * 100 + interest * i
        # Counter to find index of next value to search.
        days_to_skip = 1

        # Beginning from the current index, iterate through all all future values until a larger value is reached.
        for settle_day, settle_price in enumerate(prices[i + 1:]):
            biased_settle_price = settle_price * 100 + interest * (settle_day + i + 1)
            profit = biased_short_price - biased_settle_price

            # If the value is smaller, see if its the highest profit, then increment the ticker to skip over it later.
            if profit >= 0:
                if profit > highest_profit:
                    highest_profit = profit
                days_to_skip += 1
            # If the value is larger, immediately skip to it and begin checking profit margins with it as the short-day.
            elif profit < 0:
                break
        i += days_to_skip

    # Take one additional day interest for the day it was bought, and return the profit.
    # Return 0 if there is no possible profit, and no shares should be bought.
    if highest_profit - interest < 0:
        return 0
    return int(highest_profit - interest)


def generate_random_data() -> (int, int, List[int]):
    """
    Generate random data within problem parameters for testing.

    Can be called from main() to quickly test high quantities of data. Values can be easily altered to generate random
    data for other problems as well.

    :return: Int values generated, int interest, and a list of ints representing daily stock prices.
    """
    from random import randint

    days_to_generate = 99999
    interest = randint(1, 100)

    price_data = []
    for x in range(days_to_generate):
        price_data.append(randint(1, 100000))
    return days_to_generate, interest, price_data


main()
