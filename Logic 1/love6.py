def love6(a, b):
  return (a==6 or b==6) or ((a+b)==6) or (abs(a-b)==6)

print(love6(6,2))
print(love6(5,1))
print(love6(6,0))
print(love6(7,1))
print(love6(5,9))
