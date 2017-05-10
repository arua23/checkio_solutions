def front_times(str, n):
    if len(str)<3:
        return str*n
    else:
        return str[0:3]*n


print(front_times("Java",3))
print(front_times("Java",2))
print(front_times("Java",0))
print(front_times("Ja",3))
