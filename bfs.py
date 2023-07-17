from collections import deque

graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A'],
    'D':['B'],
    'E':['B'],
}




path = []

def BFS(graph, start):
     visited = set()
     queue  = deque()
     queue.append(start)
     visited.add(start)

     while queue:
          n=queue.popleft()
          path.append(n)
          for neighbour in graph[n]: 
               if neighbour in visited:
                    continue
               else:
                    visited.add(neighbour)
                    queue.append(neighbour)

BFS(graph,'A')

for i in path:
    print(i,end="->") 