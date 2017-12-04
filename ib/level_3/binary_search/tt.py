

def sum_to(n):
    if n == 1:
        return 1

    return sum_to(n - 1) + n

print(sum_to(5) == 15)
print(sum_to(6) == 21)


def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
