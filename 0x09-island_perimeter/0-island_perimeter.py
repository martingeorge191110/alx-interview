#!/usr/bin/python3
"""island perimeter module"""


def island_perimeter(grid):
    """return the perimeter of the island in grid"""
    total = 0

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            # Check if element is land or sea
            if (element == 0):
                continue

            # Left check
            if (j != 0 and row[j - 1] == 0):
                total += 1
            if (j == 0):
                # left edge case
                total += 1

            # Right check
            if (j != len(row) - 1 and row[j + 1] == 0):
                total += 1
            if (j == len(row) - 1):
                # right edge case
                total += 1

            # Upper check
            if (i != 0 and grid[i - 1][j] == 0):
                total += 1
            if (i == 0):
                # top edge case
                total += 1

            # Bottom Check
            if (i != len(grid) - 1 and grid[i + 1][j] == 0):
                total += 1
            if (i == len(grid) - 1):
                # bottom edge case
                total += 1

    return (total)
