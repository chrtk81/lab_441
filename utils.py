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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def five(n: int) -> bool:
    if n <= 0:
        return False
        
    while n % 5 == 0:
        n //= 5     
    
    return n == 1

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
