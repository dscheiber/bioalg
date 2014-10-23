##patterncounter, searches for number of occurrences of pattern in string
def patterncounter(string, pattern):
    count = 0
    for i in range(len(string)):
        if string[i:(i+len(pattern))] == pattern:
                  count+=1
    return count

#data = open("dataset_2_6.txt")
#string = data.read()

string="AATCCTCAGTCCTCAGTCCGCATCTCAGTCAACTCAGTCACGCCTCAGTCGGCTCAGTCTCATCTCAGTCTCTCAGTCCTCAGTCTCCTCAGTCGCGGCGACCTCAGTCGCCCGGCCAATCCTCAGTCTCTCAGTCTGAGACTCAGTCTGCTGCTCAGTCCTCAGTCTTCTCAGTCGCTTCGTTCCCTCAGTCCTACTCAGTCCCCTCAGTCGTCCCTCAGTCAATCCTCTCAGTCCCGACTCAGTCCACTCAGTCCTCAGTCGCACTCAGTCCTCAGTCGCCCTCAGTCCTCAGTCCTCAGTCTGCTCAGTCTCTGCGCTCAGTCCTCAGTCGTCTCAGTCGCTCAGTCCTCAGTCTTTCACTCAGTCCCAAGATCCTCAGTCGCTCAGTCTTAAACTCAGTCCTCAGTCCTCAGTCTACTCAGTCTCTCTCAGTCTCCTCAGTCGAACGAACTCAGTCGACTCAGTCTTCTCTCAGTCCTCAGTCGCTCAGTCGACTTTCTCAGTCCTCAGTCTGCTGGTTGCTCAGTCCTGTCTCAGTCCTCAGTCCTCACTCAGTCCTCAGTCACTCAGTCCAACTCAGTCATTCTCAGTCTCTCAGTCAAGATTCTACTCAGTCAACTCAGTCGCGGTTACAAAAGATAGCTCAGTCCCATTGATCGCTCAGTCCTCAGTCGATCTCAGTCCTCTCAGTCCTCAGTCTCACTCTCAGTCCGCTCAGTCCTCAGTCGCCTCAGTCACTCAGTCCCCTCAGTCAAACGACTCAGTCCTCGCTCAGTCCCCTCAGTCATAATCTCAGTCCTCAGTCTTCTCAGTCCTCAGTCCTCAGTCGCCTCAGTCCTCAGTCCCTGTTCTGTCTCAGTCGACCTCAGTCCTCAGTCCGCCGCTCAGTCCGACTCAGTCCTCAGTCGCTCAGTCCTCAGTCCTCAGTCCTCAGTCCTCAGTCGGGCTGCACTCAGTCCTCAGTCAAACCCCTCAGTCCTCAGTCGTTCGCGTTCTCAGTCTTCTCAGTCCGCTCAGTCGAATGCCACTCAGTCCTCAGTCGCCTCAGTCCTGCTCAGTC"
pattern = "CTCAGTCCT"

print patterncounter(string, pattern)                  
