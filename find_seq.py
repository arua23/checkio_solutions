def get_graph(grid):
    height=len(grid)
    if height:
        width=len(grid[0])
    else:
        width=0
    grid_map={grid[i][j]: [] for i in range(height)
              for j in range(width)}
    for i in grid_map.keys():
        for row in range(height):
            for col in range(width):
                if grid[row][col]==i:
                    grid_map[i].append((row,col))
    return grid_map

def four_repeatation(grid):
    i=1
    while i in grid.keys():
        if not(len(grid[i])>=4):
            del grid[i]
        i+=1
    return grid

def checkio(matrix):

    graph=get_graph(matrix)
    sorted_graph=four_repeatation(graph)
    
    for i in sorted_graph.keys():
        for x,y in sorted_graph[i]:
            diag_check=[(x+1,y+1),(x+2,y+2),(x+3,y+3),(x-1,y-1),
                        (x-2,y-2),(x-3,y-3),(x-1,y+1),(x-2,y+2),
                        (x-3,y+3),(x+1,y-1),(x+2,y-2),(x+3,y-3)]
            rev_diag_check1=[(x-1,y-1),(x-2,y-2),(x-3,y-3)]
            row_check=[(x,y+1),(x,y+2),(x,y+3)]
            col_check=[(x+1,y),(x+2,y),(x+3,y)]

            if diag_check[0] in sorted_graph[i] and diag_check[1] in sorted_graph[i] and diag_check[2] in sorted_graph[i]:
                return True
            
            elif row_check[0] in sorted_graph[i] and row_check[1] in sorted_graph[i] and row_check[2] in sorted_graph[i]:
                return True
            
            elif col_check[0] in sorted_graph[i] and col_check[1] in sorted_graph[i] and col_check[2] in sorted_graph[i]:
                return True
            elif diag_check[3] in sorted_graph[i] and diag_check[4] in sorted_graph[i] and diag_check[5] in sorted_graph[i]:
                return True
            elif diag_check[6] in sorted_graph[i] and diag_check[7] in sorted_graph[i] and diag_check[8] in sorted_graph[i]:
                return True
            elif diag_check[9] in sorted_graph[i] and diag_check[10] in sorted_graph[i] and diag_check[11] in sorted_graph[i]:
                return True

    return False       

print(checkio([
        [1, 1, 4, 1],
        [1, 1, 1, 1],
        [2, 3, 1, 6],
        [1, 7, 2, 2]
    ]))
print(checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]))
