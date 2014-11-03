import itertools

mmlist = [["$","0","0"], ["0","$","0"], ["0","0","$"]]
kmermask = ""
kmermasklist= []

def mm_kmer(kmer, maskList): #generates mismatched kmers where $ designates a mismatch point and maskList contains all variations of the mask
    kmerMasked = []
    for i in maskList:
        kmermask=kmer
        for j in range(len(i)):
            kmermask=list(kmermask)
            if i[j]=="$":
                kmermask[j]="$"
                kmerMasked.append("".join(kmermask))
    return kmerMasked

def mask_gen(k, errors): #generates sequence of 0 and $ where $ will be used for mismatches
    maskList = []
    for x in itertools.product("0$", repeat=k):
        if x.count("$") <= errors:
            maskList.append(list(x))
    print maskList
    return maskList

##def unmask_kmer(kmerMaskedList): #creates list of appropriate kmers from masked kmers
##    unmaskedList = []
##    unmaskedKmer = []
##    mmNucleotides = ["A", "T", "G", "C"]
##    for i in kmerMaskedList:
##        for j in range(i.count("$")*4):
##            for k in range(len(i)):
##                if i[k] == "$":
##                    for l in mmNucleotides:
##                    unmaskedKmer[k] ==
##    return "poop"                    
                
            
def all_patterns(x):
    return itertools.product("ACGT", repeat=x)

##def unmask(kmersMasked):
##    allPatterns = all_patterns(3)
##    for i in kmersMasked:
##        for j in i:
##            if i[j] != q[i]:
##            count+=1

def HammingDistance(p,q): # number of mismatches between strands
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count+=1
    return count

def master_gen(k): #generates sequence of 0 and $ where $ will be used for mismatches
    masterList = []
    for x in itertools.product("ATGC", repeat=k):
        masterList.append(list(x))
    return masterList

maskList2 = mask_gen(3, 1)
#mm= mm_kmer("AAA", maskList2)
##print all_patterns(3)
##
kd= {}
##count = 0
##for i in all_patterns(3):
##    print i
##    for j in mm:
##        print j
##        if HammingDistance(j,i) <= 1:
##            try:
##               kd[i] += 1
##            except KeyError:
##                kd[i]=1
##bb = {"AAA":1, "AAC":1, "ACC":1, "CCG":1, "CGA":1}
##master = master_gen(3)
##for i in bb:
##    print i
##    masked = mm_kmer(i, maskList2)
##    for j in masked:
##        print i,">",j
##        for k in list(master):
##            print k
##            if HammingDistance(j,list(k)) <= 1:
##                print j,"and",k
##                try:
##                   kd["".join(k)] += 1
##                except KeyError:
##                    kd["".join(k)]=1                
##print kd

#print master_gen(4)

nucs = ["A", "T", "G", "C"]
kmerscycling = []
kmersworking = []
kmerlist = []
mask = "$A$"
kmer = ["A", "A", "A"]
workingKmer = []
kcount = 0
for i in range(mask.count("$")):
    print "here"
    if kcount > 0:
        print "now here.."
        for j in kmerscycling:
            #print j
            for k in range(len(j)):
                if k == "$":
                    for l in range(len(nucs)):
                        k[l] = nucs[l]
                        kmerlist.append(k)
        
    else:
        workingKmer = kmer
        for j in range(len(kmer)):
            workingKmer = kmer
            print j, "should run 3 times."
            if mask[j] == "$":
                for k in range(len(nucs)):
                    print k, "should run 8 times"
                    workingKmer[j] = nucs[k]
                    print workingKmer
                    kmerscycling.append(workingKmer)
                    workingKmer = kmer
        kcount += 1

print kmerlist        
