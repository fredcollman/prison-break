import itertools
import os

from utils import Sample, write


def main() -> None:
    prisoners = int(os.environ["PRISONERS"])
    fname = filename(prisoners)
    write(fname, sample(prisoners))


def filename(prisoners: int) -> str:
    return f"sample_prisoners{prisoners}_examples.nogit.csv"


def sample(prisoners: int) -> Sample:
    half = prisoners // 2
    yield [i + 1 for i in range(prisoners)]
    yield [prisoners - i for i in range(prisoners)]
    yield [prisoners, *range(2, prisoners), 1]
    yield [2 * (i + 1) for i in range(half)] + [2 * i + 1 for i in range(half)]
    yield [2 * i + 1 for i in range(half)] + [2 * (i + 1) for i in range(half)]
    yield [half - i for i in range(half)] + [prisoners - i for i in range(half)]
    yield [*range(2, prisoners + 1), 1]
    yield [prisoners, *range(1, prisoners)]
    swaps = [(2 * i, 2 * i - 1) for i in range(1, half + 1)]
    yield list(itertools.chain.from_iterable(swaps))


if __name__ == "__main__":
    main()
