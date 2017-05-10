def checkio(words):
    lst=words.split()
    count=0
    for i in range(len(lst)):
        if lst[i].isnumeric():
            count=0
            continue
        if lst[i].isalpha():
            count+=1
            if count==3:
                return True
    return False
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
print(checkio("Hello Raihan Ahmed"))
print(checkio("Hello Raihan"))
print(checkio("Hello World hello"))
print(checkio("He is 123 man"))
    


