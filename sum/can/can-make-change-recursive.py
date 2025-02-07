def can_make_change(target, coins):
    if target == 0:
        return True
    if target < 0:
        return False
    for item in coins:
        if can_make_change(target - item, coins) is True:
            return True
    return False

# Complexity Analysis:
# O(n ^ target) time | O(target) space

# Test Cases:
print(can_make_change(6, [1, 5]))
print(can_make_change(7, [5, 3, 4, 7]))
print(can_make_change(2, [5, 3, 4, 7]))
print(can_make_change(300, [7, 14]))
    