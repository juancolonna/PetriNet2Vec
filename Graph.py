from collections import defaultdict

class Graph:
	r'''This class represents a directed graph using adjacency list representation.
	'''
	def __init__(self):
		self.graph = defaultdict(list) # default dictionary to store graph
		self.nodes = []
		self._paths = []
		
	def addNode(self, node):
		r'''Function to add an edge to graph.'''
		self.nodes.append(node)
		
	def addEdge(self, u, v):
		r'''Function to add an edge to graph.'''
		assert u in self.nodes, 'Source node is not a valid node.'
		assert v in self.nodes, 'Target node is not a valid node.'
		if v not in self.graph[u]:
			self.graph[u].append(v)

	def __find_paths_recursively(self, u, d, visited, path):
		# Mark the current node as visited and store in path
		visited[u]= True
		path.append(u)
		# If current vertex is same as destination, then add current path[]
		if u == d:
			self._paths += path + ['.']
		else:
			# If current vertex is not destination, the recur for all the vertices adjacent to this vertex
			for i in self.graph[u]:
				if visited[i]:
					self._paths += path + [i]  + ['.'] # this '.' is added to know when a final state is reached.
				else:
					self.__find_paths_recursively(i, d, visited, path) # Recursion
					
		# Remove current vertex from path[] and mark it as unvisited
		path.pop()
		visited[u] = False

	def find_all_paths(self, s, d): # Find all paths from 's' to 'd', loops are breaked into paths only one time
		r'''A recursive function to find all paths from 'u' to 'd'. 
			visited[] keeps track of vertices in current path.
			path[] stores actual vertices and path_index is current	index in path[]
		'''
		visited = {node:False for node in self.nodes} # Mark all the vertices as not visited
		path = [] # Create an array to store paths
		self.__find_paths_recursively(s, d, visited, path) # Call the recursive helper function to print all paths

		paths = []
		aux = []
		for n in self._paths:
			if n=='.':
				paths.append(aux)
				aux = []
			else:
				aux.append(n)
		
		return paths


