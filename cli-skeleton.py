#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path


def main(argv=None) -> int:
    """
    Parse CLI arguments and run pipeline.

    Args:

        argv (list[str] | None): List of arguments to parse.
            Defaults to sys.argv[1:] when None.

    Returns:
        int: Exit code (0 = success, nonzero = failure)

    Usage:
        python3 cli-skeleton.py --input data/sample.csv --output results/out.tx --verbose
    """
    p = argparse.ArgumentParser(description="Process some input/output files.")
    p.add_argument("--input", required=True, help="Path to input file")
    p.add_argument("--output", required=False, help="Optional output file")
    p.add_argument("--verbose", required=False, help="Enable verbose logging")
    args = p.parse_args(argv)

    if args.verbose:
        print(f"[INFO] Input: {args.input}, Output: {args.output}")

    # Example read input path and just print it
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[ERROR] Input file {args.input} not found.", file=sys.stderr)
        return 1

    print(f"Processing file {input_path}…")

    # TODO: Logic here
    return 0


if __name__ == "__main__":
    sys.exit(main())
