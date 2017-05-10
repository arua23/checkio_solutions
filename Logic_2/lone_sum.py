def lone_sum(a, b, c):
    if a==b and b==c and c==a:
        return 0
    elif a==b and a!=c:
        return c
    elif a==c and b!=c:
        return b
    elif b==c and c!=a:
        return a
    else:
        return a+b+c

print(lone_sum(1, 2, 3))
print(lone_sum(3,2,3))
print(lone_sum(3, 3, 3))
  
