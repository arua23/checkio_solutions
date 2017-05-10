def checkio(data):
    data.sort()
    if len(data)%2==1:
        return data[len(data)//2]
    else:
        return sum(data[len(data)//2-1:len(data)//2+1])/2
        

print(checkio([6,10,4,5,12,11,13]))
print(checkio([1, 300, 2, 200, 1]))
print(checkio([3, 6, 20, 99, 10, 15]))
print(checkio(list(range(1000000))))
