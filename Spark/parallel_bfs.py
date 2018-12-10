import sys

def parseNeighbors(line):
	nodes = line.split(" ")
	if len(nodes) > 1:
		return (nodes[0], nodes[1:])
	else:
		return (nodes[0], [])

def BFS(node_neighbors_dist):		#<node, ([neighbours], dist)>
	node = node_neighbors_dist[0]
	neighbours = node_neighbors_dist[1][0]
	dist = node_neighbors_dist[1][1]
	
	for n in neighbours:
		yield (n, dist+1)	#return a generator in form of: [(n, dist+1)]
	
	yield (node,dist)		#a node emit itself 
	
def min(list_of_values):
	min = sys.maxint
	for i in list_of_values:
		if i<min:
			min = i
	return min

	
lines = sc.textFile("dbfs:/FileStore/tables/graph.txt")
# nodes as adj. list, constant throughout iteration --> Thus, cache() avoid repeatitive computations 
nodes = lines.map(parseNeighbors).cache()
# wegiht vector to be updated repeatedly across iterations, no caching 
dists = nodes.map(lambda node: (node[0], 0 if node[0]=='0' else sys.maxint))	#init original 

# across iterations, update global rdd dists. 
for iteration in range(4):  #the iterative part
    # graph structure preserved: <const adj. list>.join(<weight vector>)
	update = nodes.join(dists).flatMap(lambda node_neighbors_dist: BFS(node_neighbors_dist))	#get <node, [list_of_distances_from_itself_to_src]>
	dists = update.reduceByKey(min)     #min, not add. Noted.

dists.sortByKey().collect()