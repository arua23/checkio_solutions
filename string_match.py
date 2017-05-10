def string_match(a,b):
    count=0;
    for i in range(len(a)-1):
        str_1=a[i:i+2]
        for j in range(len(b)-1):
            str_2=b[j:j+2]
            if str_2==str_1 and i==j:
                count+=1
    return count

print(string_match("xxa","xxa"))
print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match('aabbccdd', 'abbbxxd'))
