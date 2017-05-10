def find_message(text):
    out=""
    for i in range(len(text)):
        c=text[i]
        if c.isupper():
            out+=c
    return out
        
print(find_message('ello orld'))
