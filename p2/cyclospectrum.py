from collections import defaultdict
##def cyclospectrum(peptide):
##    massDict = {}
##    f = open("mass_table.txt", "r")
##    for i in f.readlines():
##        massDict.update({i[0]:int(i[2:])})
##    return

##def linearspectrum(peptide):
##    massDict = {}
##    f = open("mass_table.txt", "r")
##    for i in f.readlines():
##        massDict.update({i[0]:int(i[2:])})
##
##    workingPrefix = 0
##    prefixMass = [0]
##    prefixStr = []
##    for i in range(len(peptide)):
##        workingPrefix= workingPrefix + massDict[peptide[i]]
##        prefixMass.append(workingPrefix)
##        if i > 0:
##            prefixStr.append((prefixStr[i-1]+peptide[i]))
##        else:
##            print "here"
##            prefixStr.append(peptide[i])
##    print prefixStr
##    print prefixMass
##    
##    linearSpectrum = []
##    for i in range(len(peptide)-1):
##        for j in range(i+1,len(peptide)):
##            print i, prefixMass[i], prefixStr[i]
##            print peptide[j], massDict[peptide[j]],"+",prefixMass[i],"=",massDict[peptide[j]] + prefixMass[i]
##            #print massDict[peptide[j]] - prefixMass[i], prefixMass[j], prefixMass[i]
##            linearSpectrum.append(massDict[peptide[j]] + prefixMass[i])
##            #print linearSpectrum
##            
##    return linearSpectrum.sort()

def cyclicspectrum(peptide):
    fragDict = defaultdict(list)
    count = 0
    totalPeptide = 0
    massDict = {}
    f = open("mass_table.txt", "r")
    for i in f.readlines():
        massDict.update({i[0]:int(i[2:])})

    for i in peptide:
        count += massDict[i]
    totalPeptide = count    
    
    
    for i in range(len(peptide)):
        if i > 0 :
            peptide = peptide[1:]+peptide[0]
            
        for j in range(1, len(peptide)-i):

            count = 0
            split1 = [x for x in peptide[j:]]
            for k in split1:
                count += massDict[k]
            #print count,split1    
            fragDict["".join(split1)].append(count)  

            count = 0
            split2 = [x for x in peptide[:j]]
            for k in split2:
                count += massDict[k]
            #print count,split2    
            fragDict["".join(split2)].append(count)             
    print fragDict["A"]
    final = [fragDict[x] for x in fragDict]
    final.sort()
    return "0","".join(str(final)).replace(",", "").replace("[", "").replace("]", ""),totalPeptide

print cyclicspectrum("REEKEHGQHCPMHGK")
    
