def checkio(str_number, radix):
    try:
        n=int(str_number,radix)
        return n
    except ValueError:
        return -1
        
print(checkio("12",2))
