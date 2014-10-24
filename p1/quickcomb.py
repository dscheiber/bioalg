import itertools

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

print "starting itertools"
combList = itertools.product(["A","T", "G", "C"], repeat=16)
print "done and" #len(list(combList)),"length"
#print list(combList)[:-1]

print "starting generator"
genList = xselections(["A","T", "G", "C"], 16)
print "done and" #len(list(genList)),"length"
#print list(genList)[:-1]
