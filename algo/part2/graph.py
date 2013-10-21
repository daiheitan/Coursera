from time import time
t=time()
A=[]
nodes=1001
MAX=100000000000000000000
for i in range(0,nodes):
	A.append([])
	for j in range(0,nodes):
		A[i].append(MAX)
B=[]
f=open("g3.txt","r")
for line in f:
	i,j,k=(int(item) for item in line.split())
	A[i][j]=k
B.append([])
for i in range(1,nodes):
		B.append([])
		B[i].append([])
		for j in range(1,nodes):
			B[i].append([])
			if i==j:
				B[i][j]=0
			else:
				B[i][j]=A[i][j]
#check negative circle:
flag=False
answer=MAX
for k in range(1,nodes):
	for i in range(1,nodes):
		for j in range(1,nodes):
			if B[i][j]==MAX and (B[i][k]==MAX or B[k][j]==MAX):
				B[i][j]=MAX
			else:
				B[i][j]=min(B[i][j],B[i][k]+B[k][j])
			if i==j and B[i][j]<0:
				flag=True
				break
			if B[i][j]<answer:
				answer=B[i][j]
		if flag:
			break
	if flag:
		break

if flag:
	print "NULL"
else:
	print answer
print time()-t