import mysql.connector

connection = mysql.connector.connect(host='localhost',user='',password = '',db = 'pk')

cur = connection.cursor()

cur.execute("Select src,dest,cost from prim;")

rows = list(cur)

cur.close()

rows += [ (i,j,k) for (j,i,k) in rows ]

visited = set()

cur_edges = []

for i in rows:

    if i[0] == rows[0][0]:

        cur_edges.append(i)

cost = 0

edges = []

while cur_edges:

    cur_edges.sort(key=lambda x:x[2])

    minm = cur_edges[0]

    cur_edges.pop(0)

    if not minm[0] in visited or not minm[1] in visited:

        visited.add(minm[0])

        visited.add(minm[1])

        edges += [[minm[0],minm[1]]]

        cost += minm[2]

        for i in rows:

            if i[0] == minm[1]:

                cur_edges.append(i)

print("Cost - ",cost)

print("Edges : ","\n")

print(edges)
