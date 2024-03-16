# Given three lists representing take out orders, dine in orders, and the order these were
# served in, validate that all orders were served first-come, first-served.
# Time efficiency: O(n). Space efficiency: O(1).
from typing import List


def main():
    take_out_orders = [1, 3, 5]
    dine_in_orders = [2, 4, 6]
    bad_order = [1, 2, 4, 6, 5, 3]
    print(validate_fifo(take_out_orders, dine_in_orders, bad_order))

    good_order = [1, 2, 4, 3, 6, 5]
    print(validate_fifo(take_out_orders, dine_in_orders, good_order))


def validate_fifo(take_out_orders: List[int],
                  dine_in_orders: List[int],
                  served_orders: List[int]):
    take_out_index = 0
    dine_in_index = 0
    for i in range(len(served_orders) - 1):
        if take_out_index < len(take_out_orders) and served_orders[i] == take_out_orders[take_out_index]:
            take_out_index += 1
            continue
        if dine_in_index < len(dine_in_orders) and served_orders[i] == dine_in_orders[dine_in_index]:
            dine_in_index += 1
            continue
        return False

    return True


if __name__ == '__main__':
    main()
