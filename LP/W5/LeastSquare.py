from numpy import *
f=open("Data_Corr.txt","r")
points=[]
count=0
for line in f:
	t,y=(float(item) for item in line.strip().split())
	points.append((t,y))
	count=count+1
At=[]
Bt=[]
for i in range(0,count):
	t=points[i][0]
	temp=[1,t,t*t,t*t*t,t*t*t*t]
	At.append(temp)
	Bt.append([points[i][1]])
A=matrix(At)
B=matrix(Bt)
result=(A.T*A).I*(A.T)*B
print result