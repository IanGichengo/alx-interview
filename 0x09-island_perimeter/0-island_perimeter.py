#!/usr/bin/python3
"""
This module contains the island_perimeter function to calculate
the perimeter of the island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.

    Args:
        grid (list): A list of lists of integers where 0 represents water
                     and 1 represents land. Each cell is square and
                     cells are connected horizontally/vertically.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell (shared edge)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
