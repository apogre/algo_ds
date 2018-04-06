import sys

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


unvisited_nodes = {node:None for node in nodes}


visited = {}
current = "B"
currentDist = 0
unvisited_nodes[current] = currentDist


while True:
	for neighbour, distance in distances.get(current).iteritems():
		if neighbour not in unvisited_nodes: continue
		newDistance = currentDist + distance
		if unvisited_nodes[neighbour] == None or unvisited_nodes[neighbour] > newDistance:
			unvisited_nodes[neighbour] = newDistance
	visited[current] = currentDist
	del unvisited_nodes[current]
	if not unvisited_nodes: break
	candidates = [node for node in unvisited_nodes.items() if node[1]]
	print "candidates", candidates
	current, currentDist = sorted(candidates, key = lambda x:x[1])[0]
	print current, currentDist
	print "visited", visited
	print "unvisited", unvisited_nodes

print visited
