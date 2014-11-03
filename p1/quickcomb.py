import itertools

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss
string=''
print "starting itertools"
combList = [list(x) for x in itertools.product("0$", repeat=3)]
print "done and" #len(list(combList)),"length"
#print list(combList)
##print list(combList)
##for i in list(combList):
##    print "doing"
##    print i

#print "starting generator"
#genList = xselections(["A","T", "G", "C"], 2)
#print "done and" #len(list(genList)),"length"
#print list(genList)

#print list(genList)==combList

maskList = []
for x in itertools.product("0$", repeat=12):
    if x.count("$") <= 2:
        maskList.append(list(x))
print maskList
