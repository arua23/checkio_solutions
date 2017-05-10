def left2(str):
  t=str[:2]
  out=str+t
  return out[-len(str)::]

print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))
