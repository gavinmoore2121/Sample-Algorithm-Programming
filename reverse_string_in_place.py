# Given a string, reverse it in place.
from typing import List


def main():
    print(reverse_string(['R', 'e', 'v', 'e', 'r', 's', 'e', ' ', 'm', 'e']))


def reverse_string(input_string: List[chr]):
    # Iterate through list of characters and swap first and last.
    # Time efficiency: O(n). Space efficiency: O(1)
    for i in range(0, int(len(input_string) / 2)):
        input_string[i], input_string[-1 - i] = input_string[-1 - i], input_string[i]

    return input_string


if __name__ == '__main__':
    main()
