import sys
import math
from copy import copy, deepcopy
from decimal import *
getcontext().prec=20
filename=sys.argv[1]
f=open(filename,"r")
tf=open(filename+".out","w")
m,n=(int(item) for item in f.readline().split())
B=[int(item) for item in f.readline().split()]
N=[int(item) for item in f.readline().split()]
b=[Decimal(item) for item in f.readline().split()]
a=[]
for i in range(0,m):
	a.append([Decimal(item) for item in f.readline().split()])
obj=[Decimal(item) for item in f.readline().split()]
z0=obj[0]
c=obj[1:]

count=0
#define the transform method
def transform(enteringVariableIndex,leavingVariableIndex):
	global z0,c,b,B,N,a,m,n
	print "enters x"+str(N[enteringVariableIndex]),"leaves x"+str(B[leavingVariableIndex])
	trans=[]
	for j in range(0,len(N)):
		if j==enteringVariableIndex:
			trans.append(Decimal(1/a[leavingVariableIndex][enteringVariableIndex]))
		else:
			trans.append(Decimal(a[leavingVariableIndex][j])/Decimal(a[leavingVariableIndex][enteringVariableIndex])*Decimal(-1))
	transB=b[leavingVariableIndex]*Decimal(-1)/Decimal(a[leavingVariableIndex][enteringVariableIndex])
	z0=Decimal(transB)*Decimal(c[enteringVariableIndex])+z0
	t=Decimal(c[enteringVariableIndex])
	for j in range(0,len(N)):
		if j==enteringVariableIndex:
			c[j]=Decimal(trans[j])*t
		else:
			c[j]=Decimal(trans[j])*t+c[j]
	for i in range(0,len(B)):
		if i==leavingVariableIndex:
			b[i]=transB
			for j in range(0,len(N)):
				a[i][j]=trans[j]
		else:
			t=a[i][enteringVariableIndex]
			for j in range(0,len(N)):
				# print i,j
				if j==enteringVariableIndex:
					a[i][j]=Decimal(trans[j])*Decimal(t)
				#a[i][j]=1/a[leavingVariableIndex][enteringVariableIndex]*a[i][j]
				else:
					a[i][j]=Decimal(trans[j])*Decimal(t)+a[i][j]
			b[i]=Decimal(transB)*Decimal(t)+b[i]

	tmp=N[enteringVariableIndex]
	N[enteringVariableIndex]=B[leavingVariableIndex]
	B[leavingVariableIndex]=tmp
	#print N,B
def initial():
	global z0,c,b,B,N,a,m,n
	#check if the problem needs an intial
	foundNeg=False
	origc=c[:]
	orign=N[:]
	origz0=z0
	for i in b:
		if i<0:
			foundNeg=True
			break
	if foundNeg is False:
		return 0
	#add X_0 to non-basic
	N.append(0)
	#change the objective to -x_0
	
	c=[]
	for i in N:
		if i!=0:
			c.append(0)
		else:
			c.append(-1.0)
	z0=Decimal(0)
	#append a column for x_0 of every constraint
	for line in a:
		line.append(1.0)
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
		
		for i in range(0,len(B)):
			if a[i][enteringVariableIndex]>=0:
				continue
			ans=math.fabs(-1*b[i]/a[i][enteringVariableIndex])
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
		
		#if x_0 leaves, the next dict will be final
		if B[leavingVariableIndex]==0:
			final=True
		transform(enteringVariableIndex,leavingVariableIndex)
	if math.fabs(z0-0)>1e-2:
		print "Damn z0",z0
		return -1
	else:
		#get x0 index of N
		index=N.index(0)
		N.remove(0)
		#remove x0 from c
		#remove x0 from a
		for line in a:
			line.remove(line[index])
		#generate new z0,c,N
		z0=origz0
		tempCount=0
		c=[]
		for count in range(0,len(N)):
			c.append(0)
		for i in orign:
			if i in B:
				z0=z0+origc[orign.index(i)]*b[B.index(i)]
				for count in range(0,len(c)):
					c[count]=c[count]+origc[orign.index(i)]*a[B.index(i)][count]
			else:
				c[N.index(i)]+=origc[orign.index(i)]
		return 0
def pivot():
	global z0,c,b,B,N,a,m,n
	#choose an entering variable:
	#the principle: if the variable increases, z increases.
	#so we will simply check every Ci and choose the positive
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
		
		for i in range(0,len(B)):
			if a[i][enteringVariableIndex]>=0:
				continue
			ans=math.fabs(-1*b[i]/a[i][enteringVariableIndex])
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
		transform(enteringVariableIndex,leavingVariableIndex)
	if enteringVariableIndex==-1:
		return 0
	else:
		return -1
#program begins
while True:
	print "Initial"
	result=initial()
	if result is -1:
		tf.write("infeasible")
		tf.close()
		break
	print "Pivoting"
	result=pivot()
	print "Final A",a
	print "Final b",b
	#found unbounded
	if result is -1:
		tf.write("unbounded")
		tf.close()
		break
	else:
		#Now we will check every basic variable and add cut
		newcount=len(B)+len(N)
		currentCount=0
		totalCount=len(b)
		foundFloat=False
		for r in range(0,totalCount):
			i=b[r]
			if Decimal(i)-Decimal(math.floor(i))>Decimal(0.0000001) and Decimal(math.ceil(i))-Decimal(i)>Decimal(0.0000001):#not integer
				foundFloat=True
				#generate a new basic, add it to B
				B.append(newcount+1)
				newcount=newcount+1
				#generate the constraint
				newConstraint=[]
				for j in a[r]:
					newConstraint.append(Decimal(-j)-Decimal(math.floor(-j)))
				a.append(newConstraint)
				b.append(-i+Decimal(math.floor(i)))
		if foundFloat is True:
			print "Cutting!"
			# print B
			# print a
			# print b
			# print z0
			# print c
			continue
		else:
			tf.write("%.1f"%z0)
			tf.close()
			break