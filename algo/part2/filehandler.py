f=open("clustering_big.txt","r")
f1=open("newcluster.txt",'a')
for line in f:
	strr=''.join(line.split(" ")).strip()+"\n"
	f1.write(strr)
f1.close()