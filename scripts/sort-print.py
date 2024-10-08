#!/usr/bin/env python

import click

import polars as pl
import sys


@click.command()
@click.argument("in-files", nargs=-1, type=click.File(mode="r"))
def main(in_files):
    if out is None:
        out = sys.stdout

    if not in_files:
        return

    dfs = [pl.read_csv(file, separator="\t") for file in in_files]
    df = pl.concat(dfs)

    if odd:
        df = df.filter(pl.col(odd).mod(2).eq(1))

    if even:
        df = df.filter(pl.col(even).mod(2).eq(0))

    df = df.sort(sort_by)
    df.write_csv(out, separator="\t")


if __name__ == "__main__":
    main()
