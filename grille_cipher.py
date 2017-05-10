def recall_password(cipher_grille, ciphered_password):
    grid=list(cipher_grille)
    rotation=len(grid)
    out=""
    while rotation>=1:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]=="X":
                    out+=ciphered_password[i][j]
                    
        grid=list(map(list,zip(*grid[::-1])))
        rotation-=1

    return out


print(recall_password(('X...','..X.','X..X','....'),('itdf','gdce','aton','qrdi')))
