def checkio(number):
    n=str(number)
    r=1
    for i in range(len(n)):
        if n[i]!="0":
            r=r*int(n[i])

    return r

print(checkio(1000))
