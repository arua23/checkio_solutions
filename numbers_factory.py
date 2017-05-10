def checkio(num):
    ans=""
    digit=9
    while digit>1:
        if not(num%digit ==0):
            digit-=1
        else:
            ans=str(digit)+ans
            num/=digit
    if num == 1:
        return int(ans)
    else:
        return 0
        

print(checkio(200))
print(checkio(100))
print(checkio(9973))
print(checkio(30))
print(checkio(8146))
print(checkio(12))

