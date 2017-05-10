def checkio(numbers_array):
    n=list(numbers_array)
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if abs(n[j])>abs(n[j+1]):
                n[j],n[j+1]=n[j+1],n[j]

    return n

print(checkio((1, 2, 3, 0)))
print(checkio((-20, -5, 10, 15)))
print(checkio((-1, -2, -3, 0)))
