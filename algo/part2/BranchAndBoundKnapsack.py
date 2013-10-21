from collections import deque
from time import time
#this script uses 583s
ti=time()
f=open("knapsack_big.txt","r")
SIZE=2000000
ITEMCOUNT=2000
items=[]
for line in f:
	item=tuple(int(i) for i in line.split(" "))
	items.append(item)
#items.sort(key=lambda x: float(x[0])/float(x[1]))
A=deque();
B=deque();
for item in items:
	if item[1]>SIZE:
		continue
	B.clear()
	#print item
	for itemA in A:
		newitem=(item[0]+itemA[0],item[1]+itemA[1])
		if newitem[1]<=SIZE:
			B.append(newitem)
	B.append(item)
	for i in B:
		if len(A)==0:
			A.append(i)
			continue
		temp=deque()
		flag=True
		while len(A)>0:
			t=A[len(A)-1]
			if t[0]>i[0] and t[1]>i[1]:
				temp.appendleft(A.pop())
			elif t[0]<=i[0] and t[1]<=i[1]:
				A.append(i)
				flag=False
				break
			elif t[0]>=i[0] and t[1]<=i[1]:
				flag=False
				break
			elif t[0]<=i[0] and t[1]>=i[1]:
				A.pop()
		if flag is True:
			A.append(i)
		A.extend(temp)
	# print B
	# print A
item=A.pop()
print item[0]
print time()-ti
