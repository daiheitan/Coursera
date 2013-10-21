import sys
filename=sys.argv[1]
f=open(filename,"r")
tf=open(filename+".out1","w")

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
#add X_0 to non-basic
N.append(0)
#change the objective to -x_0
origc=c
origz0=z0
c=[]
for i in N:
	if i!=0:
		c.append(0)
	else:
		c.append(-1.0)
z0=0
#append a column for x_0 of every constraint
for line in a:
	line.append(1.0)
#define the transform method
def transform(enteringVariableIndex,leavingVariableIndex):
	global z0,c,b,B,N,a,m,n
	print "enter",enteringVariableIndex,"leave",leavingVariableIndex
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
	# print "trans",trans
	# print "transB",transB
	# print "z0",z0
	# print "N",N
	# print "B",B
	# print "C",c
	# print "b",b
	# print a 
#magic pivot:x_0 enters, x_j with the least value of b_j leaves
bindex=-1
leastb=1000000000000
for i in b:
	if i<leastb:
		leastb=i
		bindex=b.index(i)
#magic pivot
transform(N.index(0),bindex)
#continue with normal pivoting
enteringVariableIndex=0
leavingVariableIndex=0
#we set a flag indicating the final dict
final=False
while final!=True:
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
	
	#if x_0 enters, the next dict will be final
	if N[enteringVariableIndex]==0:
		flag=True
	transform(enteringVariableIndex,leavingVariableIndex)
#Get opt
tf.write(str(0 if z0>0 else z0))
tf.close()
