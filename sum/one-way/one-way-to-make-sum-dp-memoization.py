def one_way_to_make_sum(sum, nums, memo = None):
    if memo == None:
        memo = {}
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None
    for num in nums:
        result = one_way_to_make_sum(sum - num, nums, memo)
        if result is not None:
            memo[sum] = [num] + result
            return memo[sum]
    memo[sum] = None
    return memo[sum]

# Complexity Analysis:
# O(n * m * m) time | O(m * m) space

# Test Cases:
print(one_way_to_make_sum(6, [1, 5]))
print(one_way_to_make_sum(7, [5, 3, 4, 7]))
print(one_way_to_make_sum(2, [5, 3, 4, 7]))
print(one_way_to_make_sum(300, [7, 14]))