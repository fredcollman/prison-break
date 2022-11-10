import csv
import os
import random
import sys
from datetime import datetime
from typing import Iterator

from utils import Sample, log, write


def main() -> None:
    size = int(os.environ["SAMPLE_SIZE"])
    prisoners = int(os.environ["PRISONERS"])
    seed = init(os.environ.get("SEED"))
    fname = filename(size=size, prisoners=prisoners, seed=seed)
    write(fname, sample(prisoners=prisoners, size=size))


def init(seed: str | None) -> str:
    seed = seed or new_seed()
    log("using seed", seed)
    random.seed(seed)
    return seed


def new_seed() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")


def filename(size: int, prisoners: int, seed: str) -> str:
    return f"sample_prisoners{prisoners}_size{size}_{seed}.nogit.csv"


def sample(prisoners: int, size: int) -> Sample:
    for _ in range(size):
        yield permutation(prisoners)


def permutation(prisoners: int) -> list[int]:
    selected = [i + 1 for i in range(prisoners)]
    random.shuffle(selected)
    return selected


if __name__ == "__main__":
    main()
