import copy
import random
f=open("kargerMinCut.txt","r")
arr={}#an map
for temp in f:
	temparr=temp.split()
	key=temparr.pop(0)
	arr[key]={}
	for i in temparr:
		arr[key][i]=1
f.close()
result=100
for i in range(0,1000):#200*200*ln200, makes the probability of error to 1/n
	t=copy.deepcopy(arr)
	while len(t)>2:
		chosenNode1=t.keys()[random.randrange(0,len(t)-1)]
		chosenNodeTargets=t[chosenNode1]
		chosenNode2=chosenNodeTargets.keys()[random.randrange(0,len(chosenNodeTargets))-1]
		#chosenNode1 & chosenNode2 defines an chosen edge
		#firstly we merge these two
		for j in t[chosenNode2].keys():
			if chosenNode1 in t[j]:
				t[j][chosenNode1]+=t[j][chosenNode2]
			else:
				t[j][chosenNode1]=t[j][chosenNode2]
			del t[j][chosenNode2]
			t[chosenNode1][j]=t[j][chosenNode1]
		#secondly we remove self loops
		if chosenNode1 in t[chosenNode1].keys():
			del t[chosenNode1][chosenNode1]
		#thirdly we remove chosenNode2
		del t[chosenNode2]
	#Now we calculate the min cut
	t=t[t.keys()[0]][t.keys()[1]]
	if result>t:
		result=t
	if i%100==0:
		print "100 case passed"
print result

