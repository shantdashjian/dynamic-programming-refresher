def fib(n):
    list = [0] * (n + 1)
    list[0] = 0
    list[1] = 1
    for i in range(0, n + 1):
        if i + 1 < len(list):
            list[i + 1] += list[i]
        if i + 2 < len(list):
            list[i + 2] += list[i]
    return list[n]

# Complexity Analysis:
# O(n) time | O(n) space

# Test Cases:
print(fib(1)) # 1
print(fib(7)) # 13
print(fib(10)) # 55
print(fib(50)) # 12586269025