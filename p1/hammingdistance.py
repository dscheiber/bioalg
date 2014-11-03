import re

def HammingDistance(p,q): # number of mismatches between strands
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count+=1
    return count

##p =
##q =

#print HammingDistance(p,q)
        
def pattern_HammingDistance(pattern, text, errors): # number of patterns found in text w/ error tolerance
    indices = []
    count=0
    for i in range(len(text)-len(pattern)+1):
        workingText = text[i:i+len(pattern)]
        if workingText == pattern:
            indices.append(str(i))
        else:
            for k in range(len(workingText)):
                if workingText[k] != pattern[k]:
                   count+=1
            if count <= errors:
                indices.append(str(i))
                count = 0
            else:
                count = 0
    return  " ".join(indices) #len(indices), for count

p = "GTCATGT"
t = "GTAAATTTTGTCGAGCATCGTAGGGGTCCGAAGTGCTGAATCCGAAGCCTCTGGTGATTCAAGCTATTGTAGCGTTGGGGCGCTGATAGCGGTGTGATCTTTCCTCAGATCCCCATAGTCCGAGATCGTAGAAGAGTTCCGACTCAATCGGCAACCTAGAGGTAAGGCGATGACGCATTGGTGCACATAAGTCTGCAGAAAATGTACATCGGAAACCAGCATGAACGCTAGACCTTTCGTCACAGGCATGAAGAAGAGGACGAGAAGCGAAGTGGTGGTCGATATGACTGCTCAGCCTGGTGCCTATCCGATGTACACTAGTCCGTGGAGCCGACATCTCGTCATGTCGTTCACTGTCAACCTTGCAGCGGTGTGGCTAAACAAA"
e = 3

print pattern_HammingDistance(p, t, e)
