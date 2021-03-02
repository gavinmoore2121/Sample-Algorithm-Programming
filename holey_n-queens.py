# Holey N-Queens Batman
# @author: Gavin Moore
# 2/26/2021
# v1.1

# Description: Given an integer N (3 <= N < = 12) representing the size of a chess board, and M (0 <= M < N^2) 'holes'
# in the board at positions x y, determine the number of solutions to the N-Queens problem exist. End when the input
# 0 0 is read. Problem retrieved from Kattis.org.
#
# Expected input format:
#   N M
#   x1 y1
#   x2 y2
#   ....
#   xM yM
#
# Sample input:
# 8 0
# 8 3
# 0 3
# 5 4
# 3 7
# 0 0
#
# Sample output:
# 92
# 52
#
# Methodology:
#   - Get input
#   - Determine all possible positions for a queen in the first row.
#   - Iterate through each position, each time recursively calling the method to determine valid positions in the next
#       row and so on.
#   - Each time the method is called on a filled board, increment a global solution counter.

import sys
from typing import List

global solution_count


def main():
    """
    Main run location of the file.

    Makes calls to get input, start the solution count, and print the final number of solutions.
    """
    global solution_count
    while 1:
        board_size, num_holes, holes = get_user_input()
        if board_size == 0 and num_holes == 0:
            break
        queens_placed_rows = []
        solution_count = 0
        recursive_find_queen_positions(queens_placed_rows, board_size, holes)
        print(solution_count)


def get_user_input() -> (int, int, List[List[int]]):
    """
    Return a list of user input.

    Separates user input into values based on the format 'board_size num_holes \n hole1_x hole2_x \n ...last_hole_x
    last_hole_y'. Returns a list containing the board size, the number of holes, and a list of holes (where each hole is
    a list containing it's x coordinate in index 0 and y coordinate in index 1) in index 0, 1, and 2 respectively.

    @return: A list of categorized user input.
    """
    line = get_ints()
    board_size = line[0]
    num_holes = line[1]
    holes = [get_ints() for x in range(0, num_holes)]

    return board_size, num_holes, holes


def get_ints() -> (List[int]):
    """
    Parse an input line into integers.

    Divides a single string of whitespace-separated user-input integers from stdin into individual integers and
    saves them as a list.

    @return: A list of integers from user input.
    """
    return list(map(int, sys.stdin.readline().strip().split()))


def recursive_find_queen_positions(queens_placed_rows, board_size, holes):
    """
    Recursively find the number of possible solutions to the n-queens problem, with invalid spaces specified.

    Given a list of already placed queens, the size of the board, and the position of invalid spaces, determine the
    valid positions in the current row. Iteratively place a queen at a valid position, then recursively call this method
    to determine valid positions in the next row. Increments the global solution_count integer for each found solution.

    @param queens_placed_rows: A list of already placed queens, ordered by their row.
    @param board_size: The rows/columns of a square chess board.
    @param holes: A list containing positions of invalid spaces. Each hole is a list in the format [row, column].
    """

    current_row = len(queens_placed_rows)
    # Check if this is a valid solution
    if current_row == board_size:
        global solution_count
        solution_count += 1
        return

    # Find invalid columns based on queens
    invalid_placements = []
    for previous_row, previous_column in enumerate(queens_placed_rows):
        # Remove the vertical
        invalid_placements.append(previous_column)
        # Remove the left diagonal
        invalid_placements.append(previous_column - (current_row - previous_row))
        # Remove the right diagonal
        invalid_placements.append(previous_column + (current_row - previous_row))

    # Find invalid columns based on holes
    for hole in holes:
        if hole[0] == current_row:
            invalid_placements.append(hole[1])

    # Place self at each possible location, then call recursive_find_queen_positions to assign queens to next row.
    possible_position = [x for x in range(0, board_size) if x not in invalid_placements]
    queens_placed_rows.append(-1)
    for queen in possible_position:
        queens_placed_rows[current_row] = queen
        recursive_find_queen_positions(queens_placed_rows, board_size, holes)

    # Remove own position to prepare for next loop
    del queens_placed_rows[current_row]
    return


main()
