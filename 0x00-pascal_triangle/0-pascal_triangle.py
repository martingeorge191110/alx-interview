#!/usr/bin/env python3
from typing import List


def pascal_triangle(n: int) -> List[list]:
    """Pascal triangle"""

    if n <= 0:
        return ([])

    if n == 1:
        return ([[1]])

    if n == 2:
        return ([[1], [1, 1]])

    triangle_std = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]

        for j in range(0, len(triangle_std[-1])-1):
            a = triangle_std[-1][j]
            b = triangle_std[-1][j+1]
            temp.insert(-1, a + b)

        triangle_std.append(temp)

    return (triangle_std)
