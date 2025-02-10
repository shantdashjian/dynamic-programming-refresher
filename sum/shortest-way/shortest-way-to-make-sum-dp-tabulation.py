def shortest_way_to_make_sum(sum, nums):
    table = [None for i in range(sum + 1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] != None:
            for num in nums:
                next_index = i + num
                if  next_index < len(table):
                    if table[next_index] == None or len(table[i]) + 1 < len(table[next_index]):
                        table[next_index] = table[i] + [num]
    return table[sum]

# Complexity Analysis:
# O(n * m * m) time | O(m ^ 2) space

# Test Cases:
print(shortest_way_to_make_sum(8, [2, 3, 5]))
print(shortest_way_to_make_sum(6, [1, 5]))
print(shortest_way_to_make_sum(7, [5, 3, 4, 7]))
print(shortest_way_to_make_sum(2, [5, 3, 4, 7]))
print(shortest_way_to_make_sum(100, [1, 2, 5, 25]))
print(shortest_way_to_make_sum(300, [7, 14]))
    