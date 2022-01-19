graph = {
  'a' : ['b','d'],
  'b' : ['c','a'],
  'c' : ['b'],
  'd' : ['e','f','a'],
  'e' : ['g','f','d'],
  'f' : ['h','e','d'],
  'g' : ['h','e'],
  'h' : ['f','g']
}

visited = set()

def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, 'a')