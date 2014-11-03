def skew(string): #calculates skewed C, G content
    count=0
    countList = [0]
    for i in string:
        if i == "C":
            count-=1
        elif i == "G":
            count+=1
        countList.append(count)
    return countList

gen= "GAGCCACCGCGATA"
#skewed= skew(gen)
#print " ".join(str(x) for x in skewed)

def skew_min(string): #calculates skewed C, G content, returns indexes of minimum
    skewMin = {}
    count = 0
    minimum = 0
    #countList = [0]
    for i in range(len(string)):

        if string[i] == "C":
            count-=1
            if count < minimum:
                skewMin = {}
                skewMin[i+1] = count
                minimum = count
##                print string[i-1:i+5],i
##                print "KING OF THE CASTLE"
                
            elif count == minimum:
                skewMin[i+1] = count
##                print string[i-1:i+5],i
##                print "SHARE THE THRONE"
                
        elif string[i] == "G":
            count+=1
        elif (string[i] == "A" or string[i] == "T") and (count == minimum):
            skewMin[i+1] = count

    skewIndexes = [str(x) for x in skewMin]
    skewIndexes.sort()
    return " ".join(skewIndexes)

gen2 = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
genfile = open("sd.txt")
gen3 = genfile.readlines()[0]
gen4 = gen3[89968:]

print skew_min(gen3)
#print skew(gen4)
