def squirrel_play(temp, is_summer):
  if is_summer:
      return (temp>=60 and temp<=100 )
  else:
      return (temp>=60 and temp<=90)

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
