from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

path = []

def addEdge(x,y,c):
    graph[x].append((y,c))
    graph[y].append((x,c))

def BestFirstSearch(src,dest):
    visited = [False]*v
    pq = PriorityQueue()
    pq.put((0,src))
    visited[src] = True
    while pq.empty() == False:
        u = pq.get()[1]
        path.append(u)
        if u==dest:
            break
        for n,c in graph[u]:
            if n not in visited:
                visited[n]=True
                pq.put((c,n))





addEdge(0,1,3)
addEdge(0,2,2)
addEdge(2,3,2)
addEdge(2,4,4)
addEdge(3,5,2)
addEdge(3,6,1)
addEdge(4,6,1)


BestFirstSearch(0,6)

for i in path:
    print(i,end='->')