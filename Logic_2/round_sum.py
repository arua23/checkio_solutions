def round_sum(a, b, c):
  a=round_10(a)
  b=round_10(b)
  c=round_10(c)
  return a+b+c

def round_10(num):
    if num%10 >= 5:
        n=num+abs((num//10+1)*10-num)
        return n
    if num%10 < 5:
        n=(num//10)*10
        return n


print(round_sum(4,17,18))
print(round_sum(12, 13, 14))
print(round_sum(16, 17, 18))
print(round_sum(6,4,4))
print(round_sum(6,5,2))
