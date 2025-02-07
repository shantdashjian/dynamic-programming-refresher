def shortest_way_to_make_sum(sum, nums, memo = None):
    if memo == None:
        memo = {}
    if sum in memo:
        return memo[sum]    
    if sum == 0:
        return []
    if sum < 0:
        return None
    way = None
    for num in nums:
        result = shortest_way_to_make_sum(sum - num, nums, memo)
        if result is not None:
            if way == None:
                way = [num] + result
            elif len(result) + 1 < len(way):
                way = [num] + result
    memo[sum] = way
    return memo[sum]

# Complexity Analysis:
# O(n * m * m) time | O(m * m) space

# Test Cases:
print(shortest_way_to_make_sum(6, [1, 5]))
print(shortest_way_to_make_sum(7, [5, 3, 4, 7]))
print(shortest_way_to_make_sum(2, [5, 3, 4, 7]))
print(shortest_way_to_make_sum(100, [1, 2, 5, 25]))
print(shortest_way_to_make_sum(300, [7, 14]))