def factor(n):
    if n < 0:
        return 

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
