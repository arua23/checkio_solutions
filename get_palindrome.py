def search_first(word):
    i=len(word)
    while i>0:
        first_pal=word[0:i]
        if first_pal==first_pal[::-1]:
            return first_pal
        else:
            i-=1

def search_end(word):
    i=0
    while len(word)-i>0:
        second_pal=word[i:len(word)]
        if second_pal==second_pal[::-1]:
            return second_pal
        else:
            i+=1

def search_mid(word):
    third_pal=""
    i,j=0,len(word)
    while (j-i)>0:
        tmp=word[i:j]
        if tmp==tmp[::-1]:
            third_pal=tmp
            break
        else:
            i,j=i+1,j-1
    return third_pal

def longest_palindromic(text):
    
    first_pal=search_first(text)
    second_pal=search_end(text)
    third_pal=search_mid(text)

    if len(first_pal)>=len(second_pal) and len(first_pal)>=len(third_pal):
        return first_pal
    elif len(second_pal)>len(first_pal) and len(second_pal)>len(third_pal):
        return second_pal
    elif len(third_pal)>len(first_pal) and len(third_pal)>len(second_pal):
        return third_pal
    

print(longest_palindromic("artrartrt"))
print(longest_palindromic("madam"))
print(longest_palindromic("abc"))
print(longest_palindromic("abacaba"))
