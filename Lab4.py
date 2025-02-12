def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b

    return b


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    print(" * ".join(map(str, factors)))
