def maze2graph(maze):
    height=len(maze)
    if height:
        width=len(maze[0])
    else:
        width=0
    
            

from heapq import heappop,heappush

def heurestics(cell,goal):
    return abs(cell[0]-goal[0]+abs(cell[1]-goal[1]))


def find_path_astar(maze):
    start,goal=(1,1),(len(maze)-2,len(maze[0])-2)
    pr_queue=[]     ## priority queue
    heappush(pr_queue,(0,heurestics(start,goal), 0, "",start))
    visited=set()
    graph=maze2graph(maze)
    while pr_queue:
        _,cost,path,current=heappop(pr_queue)
        if current==goal:
            return path
        if current in visited:
            continue
        for direction,neighbour in graph[current]:
            heappush(pr_queue,(cost+heurestics(neighbour,goal)),
                     cost+1, (path+direction, neighbour))
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


print(find_path_astar(m))

                      
        
