f=open("jobs.txt","r")
data=[]
def compare(a,b):
	if a[2]==b[2]:
		return -1 if a[0]>b[0]  else 1
	if a[2]>b[2]:
		return -1
	else:
		return 1
for line in f:
	weight,length=(int(item) for item in line.split(' '))
	data.append((weight,length,float(weight)/float(length)))
data=sorted(data,cmp=compare)
print data[0:10]
answer=0
currentLength=0
for item in data:
	currentLength+=item[1]
	answer+=currentLength*item[0]
print answer

