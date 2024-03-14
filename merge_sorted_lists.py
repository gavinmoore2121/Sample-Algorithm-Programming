# Given a pair of sorted lists, merge them into a single sorted list.
from typing import List


def main():
    list1 = [3, 4, 6, 8]
    list2 = [1, 2, 5, 7]
    print(merge_sorted_lists(list1, list2))


def merge_sorted_lists(list1: List[int], list2: List[int]):
    # Iterates through both lists simultaneously and appends smaller value.
    # Appends remainder of list when one finishes early.
    # Time and space efficiency: O(n)
    list1_index = 0
    list2_index = 0
    merged_list = []

    # iterate through both arrays and add smaller value until the end of one is reached.
    while list1_index < len(list1) and list2_index < len(list2):
        if list1[list1_index] < list2[list2_index]:
            merged_list.append(list1[list1_index])
            list1_index += 1
        else:
            merged_list.append(list2[list2_index])
            list2_index += 1

    # Add remainder of whichever list hasn't finished yet
    while list1_index < len(list1):
        merged_list.append(list1[list1_index])
        list1_index += 1

    while list2_index < len(list2):
        merged_list.append(list2[list2_index])
        list2_index += 1

    return merged_list


if __name__ == '__main__':
    main()
