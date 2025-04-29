#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib",
#     "pandas",
#     "argparse",
# ]
# ///

import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read a two-column CSV from stdin and plot a bar chart as SVG."
    )
    parser.add_argument(
        "-o", "--output",
        default="chart.svg",
        help="Output SVG filename (default: %(default)s)"
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Chart title (default: no title)"
    )
    parser.add_argument(
        "--ylabel",
        default="Number of Queries",
        help="Y-axis label (default: %(default)s)"
    )
    parser.add_argument(
        "--barlabel",
        default="Queries",
        help="Label for the bar series / legend (default: %(default)s)"
    )
    args = parser.parse_args()

    # Read CSV from stdin; expect two columns: Category,Queries
    df = pd.read_csv(sys.stdin)
    categories = df.iloc[:, 0].astype(str).tolist()
    queries    = df.iloc[:, 1].astype(int).tolist()

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(categories, queries, label=args.barlabel)

    # Remove all four spines (border)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Apply title if provided
    if args.title:
        ax.set_title(args.title)

    # Apply y-axis label
    ax.set_ylabel(args.ylabel)

    # Show legend
    ax.legend(loc="upper right")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save SVG
    plt.savefig(args.output, format="svg", bbox_inches="tight")
    print(f"Saved chart as {args.output}")

if __name__ == "__main__":
    main()
