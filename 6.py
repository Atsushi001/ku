a = 2
n = 3

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

result = power(a, n)
print(f"{a}^{n} = {result}")