from itertools import permutations

def shortestPathLength(graph):
    n = len(graph)
    
    def calculate_distance(path):
        distance = 0
        for i in range(1, len(path)):
            start, end = path[i-1], path[i]
            distance += graph[start][end]
        return distance
    
    min_distance = float('inf')

    for perm in permutations(range(1, n)):
        path = (0,) + perm + (0,)
        distance = calculate_distance(path)
        min_distance = min(min_distance, distance)

    return min_distance

# Test cases
graph1 = [[1,2,3],[0],[0],[0]]
print(shortestPathLength(graph1)) 

graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(shortestPathLength(graph2)) 
