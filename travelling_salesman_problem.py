import mysql.connector as sql
from collections import defaultdict

conn = sql.connect(host='127.0.0.1',user='',password='',database='pk')

cur = conn.cursor()

cur.execute('select * from tsp')
data = list(cur)

g1 = defaultdict(list)
for i,j,k in data:
    g1[i] += [(j,k)]

# print g1


def tsp(graph):
    not_visited = set(graph.keys())
    starting = 'office'
    not_visited.remove(starting)
    current = starting
    cost = 0
    nodes = [starting]
    minimum = sorted(graph[current], key=lambda x: x[1])
    while not_visited:
        current = minimum[0][0]
        if current in not_visited:
            cost += minimum[0][1]
            not_visited.remove(current)
            minimum = sorted(graph[current], key=lambda x: x[1])
            nodes.append(current)
        
        else:
            minimum.pop(0)
    for i in graph[current]:
        if i[0] == starting:
            cost += i[1]
            nodes.append(i[0])
    print ('Minimum Cost:', cost)
    print ('Visiting Sequence:', nodes)

tsp(g1)
