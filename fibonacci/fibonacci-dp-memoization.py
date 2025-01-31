def fib(n, memo = None):
    if memo == None:
        memo = {1: 1, 2: 1}
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Complexity Analysis:
# O(n) time | O(n) space

# Test Cases:
print(fib(1))
print(fib(7))
print(fib(10))
print(fib(50))