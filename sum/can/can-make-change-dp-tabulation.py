def can_make_change(target, coins):
    table = [False for i in range(target + 1)]
    table[0] = True
    for i in range(len(table)):
        if table[i] is True:
            for coin in coins:
                if i + coin < len(table):
                    table[i + coin] = True
    return table[target]

# Complexity Analysis:
# O(m * n) time | O(m) space

# Test Cases:
print(can_make_change(6, [1, 5]))
print(can_make_change(7, [5, 3, 4, 7]))
print(can_make_change(2, [5, 3, 4, 7]))
print(can_make_change(300, [7, 14]))
    