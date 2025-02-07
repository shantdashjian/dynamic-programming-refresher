def shortest_way_to_make_sum(sum, nums):
    if sum == 0:
        return []
    if sum < 0:
        return None
    way = None
    for num in nums:
        result = shortest_way_to_make_sum(sum - num, nums)
        if result is not None:
            if way == None:
                way = [num] + result
            elif len(result) + 1 < len(way):
                way = [num] + result
    return way

# Complexity Analysis:
# O(n ^ m * m) time | O(m) space

# Test Cases:
print(shortest_way_to_make_sum(6, [1, 5]))
print(shortest_way_to_make_sum(7, [5, 3, 4, 7]))
print(shortest_way_to_make_sum(2, [5, 3, 4, 7]))
print(shortest_way_to_make_sum(300, [7, 14]))
    