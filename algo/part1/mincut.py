import copy
import random
f=open("kargerMinCut.txt","r")
arr={}#an map
for temp in f:
	temparr=temp.split()
	key=temparr.pop(0)
	arr[key]=temparr
f.close()
result=100
for i in range(0,100):#200*200*ln200, makes the probability of error to 1/n
	t=copy.deepcopy(arr)
	while len(t)>2:
		chosenNode1=t.keys()[random.randint(1,len(t))-1]
		chosenNodeTargets=t[chosenNode1]
		chosenNode2=chosenNodeTargets[random.randint(0,len(chosenNodeTargets))-1]
		#chosenNode1 & chosenNode2 defines an chosen edge
		#firstly we merge these two
		for j in t[chosenNode2]:
			t[j]=[chosenNode1 if cmp(word,chosenNode2)==0 else word for word in t[j]]
			t[chosenNode1].append(j)
		#secondly we remove self loops
		temp=t[chosenNode1]
		for j in temp[:]:
			if cmp(j,chosenNode1)==0:
				t[chosenNode1].remove(j)
		#thirdly we remove chosenNode2
		del t[chosenNode2]
	#Now we calculate the min cut
	r =len(t[t.keys()[0]])
	if result>r:
		result=r
print result
