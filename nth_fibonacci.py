# Compute the nth fibonacci number.

def main():
    print(compute_nth_fibonacci(6))


def compute_nth_fibonacci(n: int):
    # Bottom-up approach was chosen: Calc each fibonacci iteratively until target num is
    # reached. Alternative would be a recursive approach, calculating backwards, but the
    # call stack takes up unnecessary space.
    # Time and space efficiency: O(n), O(1)

    if n == 1 or n == 2:
        return 1

    last_fibonacci = 1
    second_last_fibonacci = 1

    for i in range(2, n):
        next_fibonacci = last_fibonacci + second_last_fibonacci
        second_last_fibonacci = last_fibonacci
        last_fibonacci = next_fibonacci

    return last_fibonacci


if __name__ == '__main__':
    main()
