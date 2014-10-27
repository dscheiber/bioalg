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
skewed= skew(gen)
print " ".join(str(x) for x in skewed)
