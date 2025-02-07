def grid_travel(m, n):
    if m == 1 or n == 1:
        return 1
    return grid_travel(m - 1, n) + grid_travel(m, n - 1)

# Complexity Analysis:
# O(2 ^ (m + n)) time | O(m + n) space

# Test Cases:
print(grid_travel(1, 1))
print(grid_travel(2, 3))
print(grid_travel(4, 9))
print(grid_travel(100, 100))