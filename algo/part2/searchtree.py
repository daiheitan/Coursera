#w=[0.05,0.4,0.08,0.04,0.1,0.1,0.23]
w=[0.2,0.05,0.17,0.1,0.2,0.03,0.25]
c=[]
for i in range(0,7):
	c.append([0,0,0,0,0,0,0])
def get(a,b):
	if a<=b:
		return c[a][b]
	else:
		return 0
for step in range(0,7):
	for i in range(0,7-step):
		j=i+step
		if i==j:
			c[i][j]=w[i]
		else:
			ans=1000000
			totalP=0
			for k in range(i,j+1):
				totalP=totalP+w[k]
			for r in range(i,j+1):
				temp=totalP+get(i,r-1)+get(r+1,j)
				if temp<ans:
					ans=temp
			c[i][j]=ans
print c[0][6]
