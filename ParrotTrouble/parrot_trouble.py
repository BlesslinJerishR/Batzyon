def parrot_trouble(talking, hour):
  if talking and hour < 7 :
      return True
  elif talking and hour > 20:
      return True
  else:
      return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
