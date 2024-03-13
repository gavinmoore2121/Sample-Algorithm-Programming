# Given a list of characters separated by spaces into words,
# reverse the order of the words in place.
from typing import List


def main():
    print(reverse_word_order(['R', 'e', 'v', 'e', 'r', 's', 'e', ' ',
                             'm', 'y', ' ', 'w', 'o', 'r', 'd', 's']))
    print(reverse_word_order(['h', 'e', 'l', 'l', 'o']))


def reverse_word_order(input_string: List[chr]):
    # Iterate through list of words and swap the first with the last.
    # Time efficiency: O(n). Space efficiency: O(1)
    input_string = reverse_character_list(input_string)

    current_word_start_index = 0
    for i in range(len(input_string)):
        if input_string[i] == ' ':
            input_string[current_word_start_index:i] = reverse_character_list(input_string[current_word_start_index:i])
            current_word_start_index = i + 1

    # Reverse last word
    input_string[current_word_start_index:] = reverse_character_list(input_string[current_word_start_index:])
    return input_string


def reverse_character_list(input_string: List[chr]):
    # Iterate through list of characters and swap first and last.
    # Time efficiency: O(n). Space efficiency: O(1)
    for i in range(0, int(len(input_string) / 2)):
        input_string[i], input_string[-1 - i] = input_string[-1 - i], input_string[i]

    return input_string


if __name__ == '__main__':
    main()
