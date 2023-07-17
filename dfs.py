graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A'],
    'D':['B'],
    'E':['B'],
}

visited = set()

path = []
def DFS(visited, graph, node):
    if node not in visited:
        path.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited,graph,neighbour)

DFS(visited,graph,'A')

for i in path:
    print(i,end="->") 