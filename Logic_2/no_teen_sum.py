def no_teen_sum(a, b, c):
  a=fix_teen(a)
  b=fix_teen(b)
  c=fix_teen(c)
  return a+b+c

def fix_teen(n):
    if n==15 or n==16:
        return n
    if n>=13 and n<=19:
        return 0
    return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2,13,1))
print(no_teen_sum(2,1,14))
print(no_teen_sum(1,15,3))
print(no_teen_sum(16,19,1))
