import itertools
import heapq

graph=['']
f=open('dijkstraData.txt','r')
#f=open('test.txt','r')
for line in f:
	line=line.strip(' \t\r\n')
	tmpArray=line.split('\t')
	tail=int(tmpArray[0])
	edges=[]
	for i in range(1,len(tmpArray)):
		headArray=tmpArray[i].split(',')
		#print headArray
		head=int(headArray[0])
		weight=int(headArray[1])
		edges.append(tuple((head,weight)))
	graph.append(edges)
f.close()
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(i, task, priority=0):
    'Add a new task or update the priority of an existing task'
    if i in entry_finder:
        remove_task(i)
    count = next(counter)
    entry = [priority,i, count, task]
    entry_finder[i] = entry
    heapq.heappush(pq, entry)
def get_priority(i):
	if i in entry_finder:
		return entry_finder[i][0]
	else:
		return -1
def remove_task(i):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(i)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, i, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[i]
            return (priority,task)
    return None
MAXIUM=1000000
def getans(des):
	pq=[]
	entry_finder = {}
	for i in range(1,len(graph)):
		if i>1:
			add_task(i,graph[i],MAXIUM)
		else:
			add_task(i,graph[i],0)
	while True:
		items=pop_task()
		
		if items is None:
			break
		item=items[1]
		p=items[0]
		if graph.index(item) is des:
			return p
		for edge in item:
			target=graph[edge[0]]
			tail_p=p
			target_p=tail_p+edge[1]
			head_p=get_priority(edge[0])
			# print target
			# print target_p
			# print head_p
			if target_p<head_p:
				add_task(edge[0], target,target_p)#update
	return MAXIUM
ans=[]
ind=[7,37,59,82,99,115,133,165,188,197]
#ind=[1,2,3,4]

for i in ind:
	ans.append(getans(i))
print ans
