def missing_char(str, n):
    word = ""
    for letter in str:
        if str[n] != letter:
            word += letter
        else:
            continue
    return word

print(missing_char('kitten', 0))
print(missing_char('kitten', 1))
print(missing_char('kitten', 4))
