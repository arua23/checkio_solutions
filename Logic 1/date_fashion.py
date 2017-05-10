def date_fashion(you, date):
  if (you>=8 or date>=8) and (you>2 and date>2):
      return 2
  elif you<=2 or date<=2:
      return 0
  else:
      return 1

print(date_fashion(5, 10))
print(date_fashion(5,2))
print(date_fashion(5,5))
print(date_fashion(10,2))
print(date_fashion(2,9))
