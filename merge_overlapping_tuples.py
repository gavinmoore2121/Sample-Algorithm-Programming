# Given a list of tuples, merge any that overlap into a single tuple.
# Operates in O(n * log(n)) time and O(1) space.
import operator
from typing import List


def main():
    test_case = list()
    test_case.append((0, 1))
    test_case.append((3, 5))
    test_case.append((4, 8))
    test_case.append((10, 12))
    test_case.append((9, 10))
    test_case.append((1, 2))
    test_case.append((5, 6))

    merged_tuples = merge(tuples_to_merge=test_case)

    print(merged_tuples)


def merge(tuples_to_merge: List[tuple[int, int]]) -> List[tuple[int, int]]:
    # Sort tuples in O(n * log(n)) efficiency
    tuples_to_merge.sort(key=operator.itemgetter(0))

    # For each tuple in list, check if it connects with the next one.
    # If so, combine them and remove the second.
    # O(n) efficiency
    i = 0
    num_tuples = len(tuples_to_merge)
    while i < num_tuples - 1:
        while i < num_tuples - 1 and tuples_to_merge[i][1] >= tuples_to_merge[i+1][0]:
            tuples_to_merge[i] = (tuples_to_merge[i][0], max(tuples_to_merge[i][1], tuples_to_merge[i+1][1]))
            tuples_to_merge.pop(i+1)
            num_tuples -= 1

        i += 1

    return tuples_to_merge


if __name__ == '__main__':
    main()

