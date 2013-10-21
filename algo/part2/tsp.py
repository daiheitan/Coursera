import math
from itertools import combinations 
f=open("tsp.txt","r")
cityCount=int(f.readline())
print cityCount
dist=[]
MAX=1000000000000000
for i in range(0,cityCount+1):
	dist.append([])
	for j in range(0,cityCount+1):
		dist[i].append(MAX)
count=1
dot=[[]]
while(count!=cityCount+1):
	dot.append([float(item) for item in f.readline().split()])
	count=count+1
for i in range(1,cityCount+1):
	for j in range(i,cityCount+1):
		if i==j:
			dist[i][j]=0
		else:
			dist[i][j]=dist[j][i]=math.sqrt(math.pow(dot[i][0]-dot[j][0],2)+math.pow(dot[i][1]-dot[j][1],2))
A={}
A[1]=[]
A[1].append(MAX)
A[1].append(0)
for i in range(2,cityCount+1):
	A[1].append(MAX)

for m in range(2,cityCount+1):
	print m
	s=(1<<(m-1))-1
	while s<(1<<(cityCount-1)):
		index=(s<<1)+1
		A[index]=[]
		A[index].append(MAX)
		A[index].append(MAX)
		cachingKeys.append(index)
		for j in range(2,cityCount+1):
			c=1<<(j-1)
			if (s<<1)&c!=0:#j in set
				minans=MAX
				newindex=index^c#remove j from the set
				cachingKeys.append(newindex)
				for k in range(1,cityCount+1):
					if newindex&k==0:
						continue
					ans=A[newindex][k]+dist[k][j]
					if ans<minans:
						minans=ans
				A[index].append(minans)
			else:
				A[index].append(MAX)
			#print "and with index",A[index][j]
		t=s& -s
		r=s+t
		s=(((r^s)>>2)/t)|r
finalans=MAX
finalindex=(1<<cityCount)-1
print finalindex
for j in range(2,cityCount+1):
	#print "distance",j,dist[j][1]
	if A[finalindex][j]+dist[j][1]<finalans:
		finalans=A[finalindex][j]+dist[j][1]
print finalans