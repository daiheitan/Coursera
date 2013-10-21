
from time import time
t=time()
class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}
        self.count=0

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            self.count=self.count+1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        if roots[0]==roots[1]:
        	return
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
        self.count=self.count-1
    def length(self):
    	return self.count

f=open("clustering_big.txt","r")
nodes={}
uf=UnionFind()
for line in f:
	strr=''.join(line.split(" ")).strip()
	num=int(strr,2)
	nodes[num]=strr
	#with this step we already clustered nodes with spacing 0
	uf[num]
#now cluster spacing 1
codes=[0b000000000000000000000001,
	   0b000000000000000000000010,
	   0b000000000000000000000100,
	   0b000000000000000000001000,
	   0b000000000000000000010000,
	   0b000000000000000000100000,
	   0b000000000000000001000000,
	   0b000000000000000010000000,
	   0b000000000000000100000000,
	   0b000000000000001000000000,
	   0b000000000000010000000000,
	   0b000000000000100000000000,
	   0b000000000001000000000000,
	   0b000000000010000000000000,
	   0b000000000100000000000000,
	   0b000000001000000000000000,
	   0b000000010000000000000000,
	   0b000000100000000000000000,
	   0b000001000000000000000000,
	   0b000010000000000000000000,
	   0b000100000000000000000000,
	   0b001000000000000000000000,
	   0b010000000000000000000000,
	   0b100000000000000000000000]
for num in nodes:
	for i in range(0,24):
		newnum=num^codes[i]
		if newnum in nodes:
			uf.union(num,newnum)
#now cluster spacing 2
for num in nodes:
	for i in range(0,23):
		for j in range(i+1,24):
			c=codes[i]^codes[j]
			newnum=num^c
			if newnum in nodes:
				uf.union(num,newnum)
print uf.length()
print time()-t
