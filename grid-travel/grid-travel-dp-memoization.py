def grid_travel(m, n, memo = {}):
    key = f"{min(m, n)}, {max(m, n)}"
    if key in memo:
        return memo[key]
    if m == 1 or n == 1:
        return 1
    memo[key] = grid_travel(m - 1, n) + grid_travel(m, n - 1)
    return memo[key]

# Complexity Analysis:
# O(m + n) time | O(m + n) space

# Test Cases:
print(grid_travel(1, 1))
print(grid_travel(2, 3))
print(grid_travel(4, 9))
print(grid_travel(100, 100))