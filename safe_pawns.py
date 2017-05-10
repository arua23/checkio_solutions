def safe_pawns(pawns):
    safe=0
    pawns=list(pawns)
    for i in range(len(pawns)):
        d1=chr(ord(pawns[i][0])-1)+chr(ord(pawns[i][1])-1)
        d2=chr(ord(pawns[i][0])+1)+chr(ord(pawns[i][1])-1)
        if (d1 in pawns) or (d2 in pawns):
            safe+=1

    return safe


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
