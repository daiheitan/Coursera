f=open("2sat6.txt","r")
n=int(f.readline())
graph={}
vgraph={}
mark={}
current_f=1
values={}
vvalues={}

for k in range(1,n+1):
	graph[k]=[]
	vgraph[k]=[]
	graph[-k]=[]
	vgraph[-k]=[]
for k in range(0,n):
	i,j=(int(item) for item in f.readline().split())
	graph[-i].append(j)
	graph[-j].append(i)
	vgraph[j].append(-i)
	vgraph[i].append(-j)
f.close()
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
ans={}
current_scc_num=0
def DFS2(g,v):
	global ans,current_scc_num
	current_scc_num+=1
	stack=[v]
	#print "DFS2"
	while len(stack)>0:
		#print stack
		node=stack[-1]
		ans[node]=current_scc_num
		#print "node",node
		if node not in mark:
			mark[node]=True
			for j in g[node]:
				if j not in mark:
					stack.append(j)
					if j not in caled:
						ans[j]=current_scc_num
						caled[j]=True
		else:
			stack.pop()
for i in range(n, -n-1 ,-1):
	if i==0:
		continue
	if (len(vgraph[i])>0 or len(graph[i])>0) and (i not in mark):
		DFS(vgraph,i)
flag=False
# print values
# print vvalues
mark={}
# print current_f
for i in range(current_f-1,0,-1):
	if values[i] not in mark:
		DFS2(graph,values[i])
#print ans
for i in graph:
	if i in ans and -i in ans and ans[i]==ans[-i]:
		flag=True
		break
if flag:
	print "UNSATISFIABLE"
else:
	print "SATISFIABLE"