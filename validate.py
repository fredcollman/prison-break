import csv
import sys
from typing import Callable, Iterator

from utils import Permutation, all_prisoners, log, read

Strategy = Callable[[Permutation], bool]


def main(strategy: Strategy) -> None:
    successes = 0
    total = 0
    for perm in read():
        success = strategy(perm)
        total += 1
        successes += success
    fraction = successes / total
    if successes:
        ratio = total / successes
        summary = f"(approx 1 in {ratio:.4})"
    else:
        summary = ""
    log(successes, "/", total, "=", fraction, summary)


def divide(perm: Permutation) -> bool:
    return all(divide_one(p, perm) for p in all_prisoners(perm))


def divide_one(prisoner: int, perm: Permutation) -> bool:
    half = len(perm) // 2
    if prisoner <= half:
        return prisoner in perm[:half]
    else:
        return prisoner in perm[half:]


def divide_efficient(perm: Permutation) -> bool:
    half = len(perm) // 2
    return max(perm[:half]) == half


def no_long_loops(perm: Permutation) -> bool:
    return all(no_long_loops_one(p, perm) for p in all_prisoners(perm))


def no_long_loops_one(prisoner: int, perm: Permutation) -> bool:
    half = len(perm) // 2
    box = prisoner
    seq = []
    for _ in range(half):
        found = perm[box - 1]
        seq.append(found)
        if found == prisoner:
            return True
        box = found
    return False


if __name__ == "__main__":
    STRATEGY = no_long_loops
    main(STRATEGY)
