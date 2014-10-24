from __future__ import generators

##patterncounter, searches for number of occurrences of pattern in string
def patterncounter(string, pattern):
    count = 0
    for i in range(len(string)):
        if string[i:(i+len(pattern))] == pattern:
                  count+=1
    return count
               

##patternfinder, finds most frequent k-mers; k-mers are sequences of length k.
def patternfinder (string, k):
    frequentPatterns =[]
    maxCount = 0
    for i in range(len(string) - int(k)):
        kmer = string[i:(i+k)]
        count = patterncounter(string, kmer)
        if count > maxCount:
            maxCount = count
            frequentPatterns=[]
            frequentPatterns.append(kmer)
        elif count == maxCount:        
            frequentPatterns.append(kmer)
    frequentFinal = list(set(frequentPatterns))
    return frequentFinal

def patterntonumber(pattern): ##generates all combinations of items fit to n length. matches pattern to index number in generated list.
    items=["G","C","A","T"]
    n = len(pattern)
    kmers = list(xselections(items, n))
    kmers.sort()
    return kmers.index(list(pattern))

def patterntonumber(pattern, kmers): ##pattern to number without use of generator.
    items=["G","C","A","T"]
    n = len(pattern)
    kmers = list(xselections(items, n))
    kmers.sort()
    return kmers.index(list(pattern))

def numbertopattern(index, n): ##generates all combinations of items fit to n length, converts index number to pattern in list
    items=["G","C","A","T"]
    kmers = list(xselections(items, n))
    kmers.sort()
    return kmers[index]

def NG_numbertopattern(index, n, kmers): ##number to pattern without use of generator, takes kmers argument at the end for list of kmers
    items=["G","C","A","T"]
    kmers = list(xselections(items, n))
    kmers.sort()
    return kmers[index]

def computingfrequencies(string, k): ##faster kmer finder
    frequenciesString=""
    items=["G","C","A","T"]
    kmerList = list(xselections(items, k))
    kmerList.sort()    
    frequencies = range(len(kmerList))
    for i in range(len(frequencies)):
        frequencies[i]=0
    for i in range(len(string)-k+1):
        kmer = list(string[i:(i+k)])
        index = kmerList.index(kmer)
        frequencies[index]+=1
    #print frequencies
    frequenciesString= "".join(str(frequencies))
    #print frequenciesString
    return frequenciesString
## needed to write the file for web grader
##f = open("frequencies.txt", "w")
##f.write(computingfrequencies("ACGTTTGGGTCACGCGGTCAGGGCTAGCGCTCACGTAGCCCAAATAGAGGCGTGAATGCCTAAGTTCCTCTCGTGTGCACTCTCGAGCCGGACCTGATCTATTAAGTCACGAAGGCCAACTCCCAGAGCCCACCACCTTACTCGGGTGATTCTACTCTCTCGTTTTACTACCACCGAAAGCTTGTCGTGATCCCGATCAACCGGGCACGTGGTTCACGGGAATCGAGGCCCTACCTGCTTTCTCTCGGTTCAAACCTTATACGACGTATCTTTGAGAGTTGGTCAGTATGGTACCGATTTGGTCGCTCTTGGTAAATGACAAGTATACCCACGACTTACTGCTTTACCTGTAAGAGGCTCTCTGAAATGTAACAACTACTTAAGCTCACCGCGACTGAGAGGGATCTAAAGGTGAGCTCGCCGCTCGTGGAGCACTGGAGACGGCTTCTTAGTCGCTGCTCACGACGGGTCATTGTACGCGTGCCCGGAATAACTGGTAGTAAACAATGCGATAGGTTTACGGTTGACTATAGTCACTATCAGCAACCAGCTTTGATACATCCCTGGATCAGGGTCGGGGAATGGCATAGTCGCATTTAAGCCAGCAGATTGTAGGCGAGACTATCCAACACAGTGTTGAACTCCGGATAGTTTCACCCGCTGTGCCAAAACGGACAGAATCATAGTCACGACAGCTGGGTGACCCACAACGTACGCCCATGGGCCCAGCTTGCCAGGCAGCCGCTTAATCCAATTCATCTTCATAGCCTTGAGATGAAAGTGC", 7)[1:-1].replace(",",""))
##f.close()

def computingfrequencies2(string, k, t, kmerMaster, freq): ##faster kmer finder, set to find a certain # of occurrences
##    frequenciesString=""
##    items=["G","C","A","T"]
##    kmerList = list(xselections(items, k))
##    kmerList.sort()
##    kmerListFinal=[]
##    frequencies = range(len(kmerList))
##    for i in range(len(frequencies)):
##        frequencies[i]=0
    kmerListFinal=[]

    for i in range(len(string)-k+1):
        kmer = list(string[i:(i+k)])
        print kmer
        index = kmerMaster.index(kmer)
        print index
        freq[index]+=1
        print freq[index]
        
    for i in range(len(freq)):
        if freq[i]==t:
            kmerListFinal.append("".join(kmerMaster[i]))
            #print kmerMaster[i]
    #print frequencies
    #frequenciesString= "".join(str(frequencies))
    #print frequenciesString
    #print kmerListFinal
    return kmerListFinal        

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss                

def reversecomp(x): ##makes complementary strand
    compList = []
    for i in x:
        if i == "A":
            compList.append("T")
            
        if i == "T":
            compList.append("A")
            
        if i == "G":
            compList.append("C")
            
        if i == "C":
            compList.append("G")
    return "".join(compList)[::-1]

def patterningenome(pattern, genome): #finds occurrences and position of pattern in genome
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:(i+len(pattern))] == pattern:
                  positions.append(i)
    return "".join(str(positions)).replace(",","")

def clumpfinder(genome, k, length, t):
    kmerList= []
    ########################################plucked out of computefrequencies()
    items=["G","C","A","T"]
    kmerMaster = list(xselections(items, k)) ##generates all combinations of DNA up to length k
    kmerMaster.sort()
    frequencies = [0 for x in kmerMaster] ##generates the # of frequencies needed for computefrequency2
    print frequencies
    ########################################
    for i in range(len(genome)-length):
        #print frequencies
        workingWindow= genome[i:i+length]
        kmers= computingfrequencies2(workingWindow, k, t, kmerMaster, frequencies)
        if kmers != []:
            kmerList.append(" ".join(kmers))
    return " ".join(list(set(kmerList)))
        

f = open("vc_genome.txt", "r")
vc_gen = f.read()
gen = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
        

#print clumpfinder(gen, 5, 50, 4)
print computingfrequencies(gen[:50], 5)
