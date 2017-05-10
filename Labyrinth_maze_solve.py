def dir_mapping(maze):
    height=len(maze)
    if height:
        width=len(maze[0])
    else:
        width=0
    ## assinging each maze co-ordinate to its neighbour co-ordinate
    ## and how to get to it. The dict keys are the current pos
    ## the values are neighbour and directions
    dir_map={(i,j): [] for i in range(height)
             for j in range(width) if not maze[i][j]}
    for row,col in dir_map.keys():
        if row<height-1 and not maze[row+1][col]:
            dir_map[row,col].append(("S",(row+1,col)))
            dir_map[row+1,col].append(("N",(row,col)))
        if col<width-1 and not maze[row][col+1]:
            dir_map[row,col].append(("E",(row,col+1)))
            dir_map[row,col+1].append(("W",(row,col)))
    return dir_map


from collections import deque

def find_path_bfs(maze):
    start,goal=(1,1), (len(maze)-2,len(maze[0])-2)
    queue=deque([("",start)])
    visited=set()
    graph=dir_mapping(maze)
    while queue:
        path,current=queue.popleft()
        if current==goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction,neighbour in graph[current]:
            queue.append((path+direction,neighbour))

    return "NO WAY!"



m=[ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ]

print(find_path_bfs(m))
    
        
    
        
