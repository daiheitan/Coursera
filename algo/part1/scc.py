graph={}
vgraph={}
mark={}
current_f=1
values={}
vvalues={}
f=open('SCC.txt','r')
MAXIUM=876000
for i in range(MAXIUM, 0 ,-1):
	graph[i]=[]
	vgraph[i]=[]

for line in f:
	nodes=line.split()
	tail=int(nodes[0])
	head=int(nodes[1])
	graph[tail].append(head)
	vgraph[head].append(tail)
f.close()
print "read graph"
def DFS(g,v):
	global current_f
	stack=[v]
	while len(stack)>0:
		#print stack
		node=stack[-1]
		if node not in mark:
			mark[node]=True
			for j in g[node]:
				if j not in mark:
					stack.append(j)
		else:
			if stack[-1] not in vvalues:
				values[current_f]=stack.pop()
				vvalues[values[current_f]]=current_f
				current_f+=1
			else:
				stack.pop()
	return
caled={}
def DFS2(g,v):
	counter=1
	stack=[v]
	while len(stack)>0:
		#print stack
		node=stack[-1]
		if node not in mark:
			mark[node]=True
			for j in g[node]:
				if j not in mark:
					stack.append(j)
					if j not in caled:
						counter+=1
						caled[j]=True
		else:
			stack.pop()
	return counter
for i in range(MAXIUM, 0 ,-1):
	if (len(vgraph[i])>0 or len(graph[i])>0) and (i not in mark):
		DFS(vgraph,i)
print "reversed grapgh searched"
#print values
mark={}
ans=[]
for i in range(current_f-1,0,-1):
	if values[i] not in mark:
		counter=DFS2(graph,values[i])
		ans.append(counter)
ans.sort(reverse=True)
print ans[:5]