import heapq

hlow=[]
hhigh=[]

f=open('Median.txt','r')
count=1
ans=0
for line in f:
	num=int(line)
	medium=0
	if len(hlow) is 0:
		heapq.heappush(hlow,-num)
		medium=num
	else:
		if len(hlow)>len(hhigh):#could only be 1
			if min(hlow)*-1<num:#the largest in hlow is smaller than num
				heapq.heappush(hhigh,num)
				medium=min(hlow)*-1
			else:
				heapq.heappush(hlow,-num)
				tmp=heapq.heappop(hlow)*-1
				heapq.heappush(hhigh,tmp)
				medium=min(hlow)*-1
		elif len(hlow)<len(hhigh):
			if min(hhigh)>num:
				heapq.heappush(hlow,-num)
				medium=min(hlow)*-1
			else:
				heapq.heappush(hhigh,num)
				tmp=heapq.heappop(hhigh)
				heapq.heappush(hlow,-tmp)
				medium=min(hlow)*-1
		else:
			if num<min(hhigh):
				heapq.heappush(hlow,-num)
				medium=min(hlow)*-1
			else:
				heapq.heappush(hhigh,num)
				medium=min(hhigh)
	ans+=medium
f.close()
print ans%10000
