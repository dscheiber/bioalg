import itertools

combList = ["".join(list(x)) for x in itertools.product("ATGC$", repeat=8)]
#print combList

combList2 = itertools.product("ATGC$", repeat=4)
combList3 = []
for i in combList:
    count=0
    for j in i:
        if j == "$":
            count+=1
    if count < 2:
        combList3.append(i)

print combList3
