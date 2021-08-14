def diff21(n):
    if n == 21:
        return 0
    elif n < 21:
        return 21 - n
    elif n > 21:
        return (n - 21) * 2

# Test Cases

print(diff21(19))
print(diff21(10))
print(diff21(21))
