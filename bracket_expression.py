from collections import deque

def checkio(expression):
    stack = deque([])
    pairs = {"(":")","{":"}","[":"]"}
    for i in range(len(expression)):
        if expression[i] in pairs.keys():
            stack.append(expression[i])
        elif expression[i] in pairs.values():
            if len(stack) > 0:
                opening_brace = stack.pop()
                closing_brace = pairs.get(opening_brace)
                if expression[i] != closing_brace:
                    return False
            elif i<=len(expression) and len(stack)<=0:
                return False
    if len(stack) > 0:
        return False
    return True

     
                
print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))
print(checkio("2+3"))


    
