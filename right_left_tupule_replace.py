def left_join(phrases):
    con=""
    for i in range(len(phrases)):
        con=con+phrases[i]+","

    con=con.replace("right","left")
    con=con.replace("Right","Left")
    
    return con[0:len(con)-1]

print(left_join(("right","Right")))
