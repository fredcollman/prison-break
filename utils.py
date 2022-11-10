import csv
import sys
from typing import Iterator

Permutation = list[int]
Sample = Iterator[Permutation]


def log(*msg: str) -> None:
    print(*msg, file=sys.stderr)


def write(fname: str, rows: Sample) -> None:
    log("writing to", fname)
    with open(fname, "w+", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(rows)


def read() -> Sample:
    reader = csv.reader(sys.stdin)
    for row in reader:
        yield [int(c) for c in row]
