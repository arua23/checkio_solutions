def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def mini_number(string):
    s1=string[0]
    s2=string[1]
    if int(s1)*int(s2)<=9 and len(string)>=3:
        string=str(int(s1)*int(s2))+string[2:]
        return mini_number(string)
    else:
        tmp_string=list(string)
        tmp_string.sort()
        string=""
        for i in range(len(tmp_string)):
            string+=tmp_string[i]
        return int(string)
        
def checkio(num):
    tmp=""
    end_num=num
    while end_num>1:
        for i in range(2,10):
            if end_num%i==0 and isprime(i):
                tmp+=str(i)
                end_num=end_num//i
                break
        if isprime(end_num):
            tmp+=str(end_num)
            break
    n=1
    for j in range(len(tmp)):
        n=n*int(tmp[j])
    if n!=num:
        return 0

    else:
        return int(tmp)
    
            



    
##print(checkio(33))
##print(checkio(20))
##print(checkio(3125))
##print(checkio(9973))
##print(checkio(8146))
##print(checkio(17))
##print(checkio(560))
print(checkio(12))
