#!/usr/bin/python3
"""Module for island_perimeter."""


def island_perimeter(grid):
    """Return the perimeter of the island in grid."""
    p = 0
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v:
                p += 4
                if r and grid[r - 1][c]:
                    p -= 2
                if c and row[c - 1]:
                    p -= 2
    return p
