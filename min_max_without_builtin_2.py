
def imin(*args, **kwargs):
    key=kwargs.get("key",None)
    current_min=None
    args=list(args)
    if not(key is None):
        for i in range(len(args)):
            if current_min is None or key(args[i])<key(current_min):
                current_min=args[i]

    else:
        for i in range(len(args)):
            if current_min is None or args[i]<current_min:
                current_min=args[i]

    return current_min


def imax(*args, **kwargs):
    key=kwargs.get("key",None)
    current_max=None
    args=list(args)
    if not(key is None):
        for i in range(len(args)):
            if current_max is None or key(args[i])>key(current_max):
                current_max=args[i]

        return current_max
    else:
        for i in range(len(args)):
            if current_max is None or args[i]>current_max:
                current_max=args[i]

        return current_max

print(imin(2.2, 5.6, 5.9, key=int))
print(imax(2.2, 5.6, 5.9, key=int))
print(imin([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))
print(imin("hello"))


