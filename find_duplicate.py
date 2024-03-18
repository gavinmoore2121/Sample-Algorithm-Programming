# Given a list of integers in the range 1...n, with a length of n+1, find a duplicate.
# There will be at least 1 duplicate, but may have several, and may appear more than once.
# Optimize for space efficiency, and do not modify the initial input.
from typing import List


def main():
    print(find_repeat_number([4, 3, 1, 3]))


def find_repeat_number(numbers: List[int]):
    # Sorting the list would either modify the input, or increase space complexity, so it's not viable.
    # Keeping a set of seen numbers would also increase the space complexity.

    # Because the list contains roughly all 1...n numbers, we can split the list at its midpoint,
    # and the larger half will contain the duplicate. Note this can't be recursive,
    # where the stack's space complexity would grow at log(n) rate.

    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide into upper and lower range.
        midpoint = floor + int((ceiling - floor) / 2)

        # Count items in lower range
        nums_in_lower_range = 0
        for num in numbers:
            if floor <= num <= midpoint:
                nums_in_lower_range += 1

        # If more items in lower range than expected, duplicate is in lower range
        if nums_in_lower_range > (midpoint - floor + 1):
            # Set floor and ceiling to lower range and repeat
            floor, ceiling = floor, midpoint
        else:
            # If duplicate in higher range, set floor/ceiling to higher range and repeat
            floor, ceiling = midpoint + 1, ceiling

    # Exit loop when floor == ceiling. Duplicate was found.
    return floor


if __name__ == '__main__':
    main()
