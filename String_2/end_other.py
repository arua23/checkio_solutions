def end_other(a, b):
    a=a.lower()
    b=b.lower()
    if len(a)>=len(b):
        return a[-len(b)::1]==b
    return b[-len(a)::1]==a

print(end_other("Hiabc","abc"))
print(end_other("AbC","Hiabc"))
print(end_other("abc","abXabc"))

##Other Method

##def end_other(a, b):
##  a = a.lower()
##  b = b.lower()
##  return (b.endswith(a) or a.endswith(b))
