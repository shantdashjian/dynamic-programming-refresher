def can_make_change(target, coins, memo = None):
    if memo == None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for item in coins:
        remainder = target - item
        memo[remainder] = can_make_change(remainder, coins, memo)
        if memo[remainder] is True:
            return True
    memo[target] = False
    return False

# Complexity Analysis:
# O(n * target) time | O(target) space

# Test Cases:
print(can_make_change(6, [1, 5]))
print(can_make_change(7, [5, 3, 4, 7]))
print(can_make_change(2, [5, 3, 4, 7]))
print(can_make_change(300, [7, 14]))
    