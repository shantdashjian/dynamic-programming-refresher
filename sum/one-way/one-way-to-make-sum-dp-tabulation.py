def one_way_to_make_sum(sum, nums):
    table = [None for i in range(sum + 1)]
    
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in nums:
                if i + num < len(table):
                    table[i + num] = table[i] + [num]
    return table[sum]

# Complexity Analysis:
# O(m ^ 2 * n) time | O(m * m) space

# Test Cases:
print(one_way_to_make_sum(6, [1, 5]))
print(one_way_to_make_sum(7, [5, 3, 4, 7]))
print(one_way_to_make_sum(2, [5, 3, 4, 7]))
print(one_way_to_make_sum(300, [7, 14]))
    