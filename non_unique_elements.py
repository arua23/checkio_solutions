def checkio(data):
    out=[]
    for i in range(len(data)):
        if data.count(data[i])>1:
            out.append(data[i])

    return out
