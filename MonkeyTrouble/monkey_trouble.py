def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False

t1 = monkey_trouble(True, True)
t2 = monkey_trouble(False, False)
t3 = monkey_trouble(True, False)

print(t1)
print(t2)
print(t3)
