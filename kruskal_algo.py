from collections import defaultdict
import mysql.connector
conn = mysql.connector.connect(host='localhost',
                                    database='******',
                                    user='*****',
                                    password='****')
crsr = conn.cursor()
class GRAPH:

	def __init__(self,vertices):
		self.V= vertices
		self.graph = []

	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		else :
			parent[yroot] = xroot
			rank[xroot] += 1

	def kruskal(self):
		
	"""Function for finding the minimum cost spanning tree"""

		result =[]
		i = 0
		e = 0

		self.graph = sorted(self.graph,key=lambda item: item[2])

		parent = [] ; rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		while e < self.V -1 :

			u,v,w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent ,v)


			if x != y:
				e = e + 1
				result.append([u,v,w])
				self.union(parent, rank, x, y)

		print ("Following are the edges in the constructed MST")
		for u,v,weight in result:
			print ("%d -- %d == %d" % (u,v,weight))

g = GRAPH(6)
arr = """SELECT src,dest,cost FROM pk """
crsr.execute(arr)
rows = crsr.fetchall()
for i in rows:
	print(i)
	g.addEdge(i[0],i[1],i[2])
g.kruskal()
crsr.close()
conn.close()
