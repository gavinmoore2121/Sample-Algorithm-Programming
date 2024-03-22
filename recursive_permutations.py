# Write a recursive function for generating all permutations
# of an input string. Return them as a set.
# Time and space efficiency are both poor; this is a demonstrative approach, not an optimized one.

def main():
    for perm in generate_string_permutations('recursive'):
        print(perm)


def generate_string_permutations(string: str) -> set[str]:
    # Remove the character, and call this method recursively to generate all possible permutations
    # of the string remainder. Add the character back in at all possible positions, and return the
    # resulting set. Time and space efficiency: O(n^2)

    # Case: Only one character
    if len(string) == 1:
        return set(string)

    # Case: Multiple chars remaining. Remove a char and get the resulting shuffle.
    last_char = string[-1]
    remaining_string = string[:-1]

    shuffled_substrings = generate_string_permutations(remaining_string)

    permutations = set()
    for substring in shuffled_substrings:
        for i in range(len(substring) + 1):
            permutations.add(substring[:i] + last_char + substring[i:])
    return permutations


if __name__ == '__main__':
    main()
