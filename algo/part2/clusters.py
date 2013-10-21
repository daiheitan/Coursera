from operator import itemgetter, attrgetter

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
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
        self.count=self.count-1
    def length(self):
    	return self.count

f=open("clustering1.txt",'r')
ref=[]
#we need a union-find data structure
uf=UnionFind()
for line in f:
	items=[int(item) for item in line.split(" ")]
	ref.append(items)
	uf[items[0]]
	uf[items[1]]
ref.sort(key=lambda x:x[2])
print ref[0],ref[1],ref[2],ref[3]
arrayPointer=0
while uf.length()>4:
	items=ref[arrayPointer]
	arrayPointer=arrayPointer+1
	if uf[items[0]] is not uf[items[1]]:
		uf.union(items[0],items[1])
while arrayPointer is not len(ref):
	items=ref[arrayPointer]
	arrayPointer=arrayPointer+1
	if uf[items[0]] is not uf[items[1]]:
		print items[2]
		break
print 0


