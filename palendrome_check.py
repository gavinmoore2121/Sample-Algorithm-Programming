# Given an input string, check if ANY permutation of it is a palindrome.
import string


def main():
    print(check_permutations_palindrome("civic"))
    print(check_permutations_palindrome("civil"))
    print(check_permutations_palindrome("ivicc"))


def check_permutations_palindrome(input_string: string):
    unmatched_letters = set()

    for char in input_string:
        if char in unmatched_letters:
            unmatched_letters.remove(char)
        else:
            unmatched_letters.add(char)
    return len(unmatched_letters) < 2


if __name__ == '__main__':
    main()
