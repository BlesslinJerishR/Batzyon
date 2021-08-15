def near_hundred(n):
    if n in range(90,111):
        return True
    elif n in range(190,211):
        return True
    else:
        return False

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
