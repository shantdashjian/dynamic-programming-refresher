def grid_travel(m, n):
    table = [[0 for i in range(n + 1)] for j in range(m + 1)]
    table[1][1] = 1
    for row in range(m + 1):
        for column in range(n + 1):
            if row + 1 <= m:
                table[row + 1][column] += table[row][column]
            if column + 1 <= n:
                table[row][column + 1] += table[row][column]
    return table[m][n]

# Complexity Analysis:
# O(m * n) time | O(m * n) space

# Test Cases:
print(grid_travel(1, 1))
print(grid_travel(2, 3))
print(grid_travel(4, 9))
print(grid_travel(100, 100))