# Given an integer representing flight time, and a list of integers representing movie times,
# check if two movies exist whose sum duration equals flight duration.
from typing import List


def main():
    print(check_movie_sums(10, [1, 3, 6, 8]))
    print(check_movie_sums(10, [1, 2, 4, 6, 7]))


def check_movie_sums(flight_length: int, movie_lengths: List[int]):

    # Create hash for movie lengths already viewed for O(1) checks backwards
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        if flight_length - first_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False


if __name__ == '__main__':
    main()
