import sys
filename=sys.argv[1]
f=open(filename,"r")
tf=open(filename+".out","w")
m,n=(int(item) for item in f.readline().split())
B=[int(item) for item in f.readline().split()]
N=[int(item) for item in f.readline().split()]
b=[float(item) for item in f.readline().split()]
a=[]
for i in range(0,m):
	a.append([float(item) for item in f.readline().split()])
obj=[float(item) for item in f.readline().split()]
z0=obj[0]
c=obj[1:]
#choose an entering variable:
#the principle: if the variable increases, z increases.
#so we will simply check every Ci and choose the positive
enteringVariableIndex=0
leavingVariableIndex=0
count=0
while True:
	# print "currentC",c
	enteringVariableIndex=-1
	currentMinIndices=1000000000000
	for i in range(0,len(c)):
		if c[i]>0 and N[i]<currentMinIndices:#increasing variable
			currentMinIndices=N[i]
			enteringVariableIndex=i
	if enteringVariableIndex==-1:
		break
	#now we calculate the leaving variable
	#by looping every formula
	currentMinX=1000000000000
	leavingVariableIndex=-1
	currentMinIndices=1000000000000
	
	for i in range(0,m):
		if a[i][enteringVariableIndex]>=0:
			continue
		ans=-1*b[i]/a[i][enteringVariableIndex]
		if ans>=0:
			if ans<currentMinX:
				currentMinX=ans
				leavingVariableIndex=i
				currentMinIndices=B[i]
			elif ans==currentMinX and B[i]<currentMinIndices:
				currentMinIndices=B[i]
				leavingVariableIndex=i
	if leavingVariableIndex==-1:
		break
	print "enter",enteringVariableIndex,"leave",leavingVariableIndex
	#now we transform the matrix
	trans=[]
	for j in range(0,n):
		if j==enteringVariableIndex:
			trans.append(1/a[leavingVariableIndex][enteringVariableIndex])
		else:
			trans.append(a[leavingVariableIndex][j]/a[leavingVariableIndex][enteringVariableIndex]*(-1))
	transB=b[leavingVariableIndex]*(-1)/a[leavingVariableIndex][enteringVariableIndex]
	z0=transB*c[enteringVariableIndex]+z0
	t=c[enteringVariableIndex]
	for j in range(0,n):
		if j==enteringVariableIndex:
			c[j]=trans[j]*t
		else:
			c[j]=trans[j]*t+c[j]
	for i in range(0,m):
		if i==leavingVariableIndex:
			b[i]=transB
			for j in range(0,n):
				a[i][j]=trans[j]
		else:
			t=a[i][enteringVariableIndex]
			for j in range(0,n):
				# print i,j
				if j==enteringVariableIndex:
					a[i][j]=trans[j]*t
				#a[i][j]=1/a[leavingVariableIndex][enteringVariableIndex]*a[i][j]
				else:
					a[i][j]=trans[j]*t+a[i][j]
			b[i]=transB*t+b[i]

	tmp=N[enteringVariableIndex]
	N[enteringVariableIndex]=B[leavingVariableIndex]
	B[leavingVariableIndex]=tmp
	count=count+1
	# print "trans",trans
	# print "transB",transB
	# print "z0",z0
	# print "N",N
	# print "B",B
	# print "C",c
	# print "b",b
	# print a
#found unbounded
if leavingVariableIndex is -1:
	tf.write("UNBOUNDED")
	tf.close()
else:
	tf.write(str(z0)+"\n")
	tf.write(str(count))
	tf.close()
