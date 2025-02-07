def fib(n):
    if n <= 1:
        return n
    list = [0] * (n + 1)
    list[0] = 0
    list[1] = 1
    for i in range(2, n + 1):
        list[i] = list[i - 1] + list[i - 2]
    return list[n]

# Complexity Analysis:
# O(n) time | O(n) space

# Test Cases:
print(fib(1))
print(fib(7))
print(fib(10))
print(fib(50))