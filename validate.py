import csv
import sys
from typing import Callable, Iterator

from utils import Permutation, log, read

Strategy = Callable[[Permutation], bool]


def main(strategy: Strategy) -> None:
    successes = 0
    total = 0
    for perm in read():
        success = strategy(perm)
        total += 1
        successes += success
        # print(perm, success)
    log(successes, "/", total, "=", successes / total)


def divide(perm: Permutation) -> bool:
    return all(divide_one(p, perm) for p in perm)


def divide_one(prisoner: int, perm: Permutation) -> bool:
    half = len(perm) // 2
    if prisoner <= half:
        return prisoner in perm[:half]
    else:
        return prisoner in perm[half:]


if __name__ == "__main__":
    STRATEGY = divide
    main(STRATEGY)
