def lucky_sum(a, b, c):
  sum=0
  if a!=13:
      sum=+a
      if b!=13:
          sum+=b
          if c!=13:
              sum+=c
  return sum


print(lucky_sum(1,2,3))
print(lucky_sum(1,2,13))
print(lucky_sum(1,13,3))
print(lucky_sum(13,2,3))
