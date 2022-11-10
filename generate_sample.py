import csv
import os
import random
import sys
from datetime import datetime
from typing import Iterator

Sample = Iterator[list[int]]


def log(*msg: str) -> None:
    print(*msg, file=sys.stderr)


def permutation(prisoners: int) -> list[int]:
    selected = [i + 1 for i in range(prisoners)]
    random.shuffle(selected)
    return selected


def new_seed() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")


def init(seed: str | None) -> str:
    seed = seed or new_seed()
    log("using seed", seed)
    random.seed(seed)
    return seed


def sample(prisoners: int, size: int) -> Sample:
    for _ in range(size):
        yield permutation(prisoners)


def filename(size: int, prisoners: int, seed: str) -> str:
    return f"sample_prisoners{prisoners}_size{size}_{seed}.nogit.csv"


def write(fname: str, rows: Sample) -> None:
    log("writing to", fname)
    with open(fname, "w+", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(rows)


if __name__ == "__main__":
    size = int(os.environ["SAMPLE_SIZE"])
    prisoners = int(os.environ["PRISONERS"])
    seed = init(os.environ.get("SEED"))
    fname = filename(size=size, prisoners=prisoners, seed=seed)
    write(fname, sample(prisoners=prisoners, size=size))
