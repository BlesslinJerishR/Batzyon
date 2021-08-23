def not_string(str):
    if 'not' in str[0:3]:
        return str
    else:
        return 'not ' + str


print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
