def sleep_in(weekday, vacation):
    if not weekday and not vacation:
        return True
    elif not weekday and vacation:
        return True
    elif weekday and vacation:
        return True
    elif weekday and not vacation:
        return False

r1 = sleep_in(False, False)
r2 = sleep_in(True, False)
r3 = sleep_in(False, True)
r4 = sleep_in(True, True)

print(r1)
print(r2)
print(r3)
print(r4)
