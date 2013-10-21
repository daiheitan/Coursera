f=open("knapsack1.txt",'r')
SIZE=10000
ITEM_COUNT=100
items=[]
items.append((0,0))
for line in f:
	item=tuple(int(i) for i in line.split(" "))
	items.append(item)
f.close()
A=[]
def get(a,b):
	if a<0 or b<0:
		return 0
	else:
		return A[a][b]
for i in range(0,ITEM_COUNT+1):
	A.append([0 for j in range(0,SIZE+1)])
for i in range(1,ITEM_COUNT+1):
	for j in range(0,SIZE+1):
		A[i][j]=max(get(i-1,j),get(i-1,j-items[i][1])+items[i][0] if j-items[i][1]>=0 else 0)
print A[ITEM_COUNT][SIZE]