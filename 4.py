a = 2
n = -3


def power(a, n):
    result = 1

    if n < 0:
        a = 1 / a
        n = -n

    for _ in range(n):
        result *= a

    return result

result = power(a, n)
print(result)