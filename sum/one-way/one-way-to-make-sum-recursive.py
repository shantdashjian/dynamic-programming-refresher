def one_way_to_make_sum(sum, nums):
    if sum == 0:
        return []
    if sum < 0:
        return None
    for num in nums:
        result = one_way_to_make_sum(sum - num, nums)
        if result is not None:
            return [num] + result
    return None

# Complexity Analysis:
# O(n ^ target) time | O(target) space

# Test Cases:
print(one_way_to_make_sum(6, [1, 5]))
print(one_way_to_make_sum(7, [5, 3, 4, 7]))
print(one_way_to_make_sum(2, [5, 3, 4, 7]))
print(one_way_to_make_sum(300, [7, 14]))
    