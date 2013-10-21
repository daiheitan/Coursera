from time import time
import heapq
t=time()
f=open("edges.txt","r")
graph={}
vertices=[]
for line in f:
	node1,node2,cost=(int(item) for item in line.split(' '))
	if node1 not in graph.keys():
		graph[node1]=[]
	if node2 not in graph.keys():
		graph[node2]=[]
	heapq.heappush(graph[node1],(cost,node2))
	heapq.heappush(graph[node2],(cost,node1))
vertices=graph.keys()[:]
found=[]
found.append(1)
vertices.remove(1)
answer=0
count=499
while count is not 0:
	count-=1
	known=[]
	for vertex in found:
		while len(graph[vertex]) is not 0:
			target=min(graph[vertex],key=lambda x:x[0])
			if target[1] in vertices:
				known.append((target[0],target[1],vertex))
				break
			else:
				heapq.heappop(graph[vertex])
	if len(known) is not 0:
		cost,get,orig=min(known,key=lambda x:x[0])
		heapq.heappop(graph[orig])
		found.append(get)
		vertices.remove(get)
		answer+=cost;
print answer
print time()-t