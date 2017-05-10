def double_char(str):
  str2=""
  for i in range(len(str)):
      str2+=str[i]*2
  return str2

print(double_char("Hello"))
print(double_char("Hey-you"))
print(double_char('The'))
print(double_char("AAbb"))
print(double_char('Hi-There'))
