import bisect

f=open('2sum.txt','r')
ptable={}
ntable={}
anshash={}
for line in f:
	num=int(line)
	if num<0:
		ntable[num]=True
	else:
		ptable[num]=True
n=ntable.keys()
n.sort()
p=ptable.keys()
f.close()
print "file fin"
answer=0
for j in p:
	tmpn=n[bisect.bisect_left(n,-10000-j):bisect.bisect_right(n,10000-j)]
	for k in tmpn:
		if j+k>=-10000 and j+k<=10000:
			if j+k not in anshash:
				anshash[j+k]=1
print len(anshash)