from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def translate(sequence):
    messenger_rna = Seq(sequence, IUPAC.unambiguous_rna)
    return messenger_rna.translate()

sequence = ""


##def combos_for_aminos(sequence):
##    from Bio.Data import CodonTable
##    standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
##    mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]

aminoDict ={}
aminoDict["phe"] = 2
aminoDict["leu"] = 6
aminoDict["ile"] = 3
aminoDict["met"] = 1
aminoDict["val"] = 4
aminoDict["ser"] = 6
aminoDict["pro"] = 4
aminoDict["thr"] = 4
aminoDict["ala"] = 4
aminoDict["tyr"] = 2
aminoDict["*"] = 3
aminoDict["his"] = 2
aminoDict["gln"] = 2
aminoDict["asn"] = 2
aminoDict["lys"] = 2
aminoDict["asp"] = 2
aminoDict["glu"] = 2
aminoDict["cys"] = 2
aminoDict["trp"] = 1
aminoDict["arg"] = 6
aminoDict["gly"] = 4

aa_seq = ["val", "lys", "leu", "phe", "pro", "trp", "phe", "asn", "gln", "tyr"]
##
##count = 1
##for i in aa_seq:
##    count = aminoDict[i] * count
##    print count

f = open("codon_table.txt", "r")
codon_dict = {}
for i in f.readlines():
    codon_dict.update({i[:3]: i[4]})

sequence = "ACGACCCCAATCTATACATCGGACGGACCCGGCGGATCACTTCAAACGCATAAGTTAGATTCTCTAGTGCTAACGTGGCTCATTGACCATACCTGGTAGCATCTGGGGGAGTAAAATTGACCGAAAGACACAGCTCGTGATTGGGCGACCAGAGGACATACTCGGTGCTCAGGTTTAGCCACGGGTCTGGCGGATTACTGGGAGTTGGGTAGCACTCGTGGATCGCTAGCTACCGCTTCGGCCAGGTCACGAATGTTACCCTACACCAAGCCATCTCCATCATTTTCCATTCGACTTGCAGGAAACCAAGGGACGCCTGTCCTTATATCCAGTGGGAAATATCAGTCCTCAGCACTATAACCGACTATTCACCTGGTGAGCAGATTGATTTGGTCTAAGTGATCATCCACTGGATTCCTTCTCTAGACCTGAAATGTGCATAGGTGACCACTTATGGTAAGATGTTTGTCAAGTGTTAAAGGCAAATTGGGGTGATATGTCGCTGCTTACTTTCCTGGATACATCAGAAGGATGCTGCTGCCTACTATCGCGAGTAGTCCGTTAAAACACGATGTGCACGCTCTACAAATTCGTTATCTGCTCGAGAGGCGTCTGGTCCTCTCCTTATGCGCCAGGGGCATTTATCCCTTGCCGAGACACGAAACTGAAGTCTCGTACAGTGCGCCGTCATCGCCCTGGTCAGATAGTAGAGTACACGCTCCGGTGCTCAACAGCTTTGTCATGGAAAATTTGAGGGGTATACGCCACCTTTAGTATTGGTGCCGAATAATGGAGCCCACTCCGGGCACGCGTAGAAAGGTATAGGGCGCACGGGTATTGGGCATAATCGTTGGAAGGCATAAATCCCCAGACAAACGTGGGCACCTTAAGGTGCTGGCACATCTCTCGACAGGAGGCTTCATTGGTTTCCAGCTTAGGCACAACCTCCGGCGGGCTCCGCTACAGAGCTATCAAATGGATGCGAGCTACGTCGTTTCTAGGACCACATTCAGGAGAGGTTGTGAGTCAGAAATTATCTGTCCAAGGACGGGGCGCTTAGTTTACAGTGGAGGCAAGACGTCCGGTCACGAATGCTACCCGACGCCGAGTCTGGCTATAGGGAAGTCTAGCCGTCTTGAGGACGACCAAGGTATTCAAACTGACCGTCTCCATAGAGTTAGACAATTCACCATCTCGCATTGCCGGCCCAGCCGCACTAGGCGTCGGGTAGCACTCATGCATGAATCCACGATCGTATCGATGTTCATTGGTGGTACTCAGCCAGCAGAGCTGGTGTACCACCAGACAACATGGAGTGCTTTTAAGGACCCGCTTGAGACTTATTTTTCGTGTCCCGTATCGGTATACGTGTTTTTCCTTCGCCCTGCGCTCTAACCCACCTATCACTTGCTTCGAGGTGTAACAATCCCCTGCTGTCTGTAGACATTTCATTTTATTGCATTAGGTACGATCTCTCGCCATAGTAGTCTTTGAACGCTAGGAGTCGGGTAACACTCGTGTTAGCAATATATAGGCGCAGCAGCGGTTTCACTGCTCTGACGCATTGATTGGGCTGCGTGTACAATTATCAGAAAAATTTGGCCCAGAAGGCCGGCCAATGAGTGGCGGCGCCCTATATTAGCCCAGTATGACCCGGGAAGCACGAGTGTTATCCTACTCCTAGTCGTCCCTCAGCCGCACGGATTCCTGCAACGTCTCATTGTGTTCAGACTTCTAAAACGGTCTTGGCACATCAACTGTTTTGTCTCTAGACGTGCGGGACGGCGTAGGATAACATTCGTGCGGTTGTCCTAAACGTGGACCCCGTCAATTAGTACCAATAACGCATGGGTGCTGACATGCCTTCTCGATTGTAGGCTGGCCGAGGCGGCATAAGACACATTCCCGACCCCCACGAGTGTTATCCCACGCCTTCTAAAGTTCGGCGCAGCAATCCCGGATCTCAGCTGCACCCGAAAGTAGTGATCATAAGTGAGTCTATCTCGGCCTAAACTGTACCCGATAGAGCCGTGTCAGATTCCCGGAGGAACGAATAGCTGTTTGTACGCCTATACAGGCACCGGTGGTGGAGCGCGTTTTTCCAGTCGCACGGCATTGGCTGAAAAGCGTCAACATGCGATTCGCGGTGCACTGTAGCGCTCTGAAACTCCCATGCTTTTATCGTGTTCTCCCGGATTAAGGGGACCAGAGAGACTTTTGAATAGTGCGAACGCTCTTGCAGCCATGCCCCAGACGTCCTCACTGAGGGTGAATATTATGAACATCTGAAAAAACGGCCTGACTTTTAGGCGTCGTCGCAGACGAGGTACAACTTGCAGTCAGATATCCCAGGTCTAGTCCTGATATGCTTCATAGCCTCCTGACCCTGGCATAAATACGATGGCATAATGCGCTCTAACTAACCGGGGCATCGTCGCATGGCAGCGAAGAGGCAGAGGAAGGAAGCGAGTACAATCGACCGCATTGGCTTCATTCTGTGTCTTCTTGGTATCTGGAACTAGCTTCTGTAATTTACTCGGAGTCGGATAACACTCGTGAGGTCGACCCTCCGCCCAAGGTGACCTGTGGGTCTAGGGGAGTCCCTGTAGTCTTTTGGCATGTCCAGTGTACCCTATTGTTAACTCCCGTGGGTTCATATGAAGGGCCATACCCAAGTGTCTGGGGATCTATCCCGAAAACAACGCTTCCAGATCCCGGTACGTGGATCCGGGCATGATAAGCAGAAAGGTCATGGGCCATACCCGCCTCAGTCTTCCGATGTGGTGTATGATTGTAAGCCCCTGTAAGTACCTGACCTCGGCGTATTATCTGAAATAGCCTTCGCTTCACAATCCCGGGTGTGGGAAGGAGTAAGGCCATGGATTGGCAAGAAATAGACCCTGCTAGCTGGAGGCTCATACTTTTACATAATGGCTCTGATAGCAAATGATGGTATCTCCCGCAAAATTCTAATTAGCCTACGCGACTATCCCGATGCGGTGCTACCCGCTCCACGTCCCGTCATCACACGATTAGCACCGAAGTATAGGTAAACTAGTCAGCACCCTACACGTGCGTCAATTGCTGAGGGAAATCGGTATCCGGCGTTAACACATCCCTGCTCTGTGAGAGGGCGCGACCAAGACCTACCACTATAGAGCCGATATAAGATGAAAACTAAGGTTTGTCTCGCAAAAACTTCCAAGGCGCATACCACTAGCATATGTACGAGTCCGCTGTCGGCCGGTGCAGAAGCGATTGACGTGGTATGCATTACGGAGATTACAATTTATTTGAAAGAGAGCGTTACCACACCTGGCAGTACAGAAGCATTTGTCCACGCACGTCGGCGCTGTGTCATGTCATTACATTCGCACATCCTCGAAGACAGGGTTAGAGGCTCACGTCTTCCCGCCTGTAATCCGGAGGGTTATTCCATAAGGGGTACGCCTGGGCACCAACGGGGTTAGGCAGGACATAGTTGACTGGCAATGGAAGATAGCCAGATGCCCGCTCACCTGGGACAACTCCTCACAGATAAAAGCAGATCACATACGGACGCCCGGACTCGCTGTTGCCGATGAGGTATAGCCAGGCCGATGCATCATCTCCATCCACCTTGATATCCGTAGCCAATTTGGATAGAATTGAGTATTCGCTACTGGCATCCCACGGAACCACTATTGCCACGCCATGTTCTGTAAAGGGGACGACTCTACAGAAATGCGTCGCGGTTTCACCAATCTGGAGCCAAATACAATATTTCGTCCGGTCTGTGTTGTAATAACACTTAAAATTTCTGGTGGCTTAGCTCCGCTATAACCGTAGGTCAACTTACCGCGTGGACTAGCTCATTTAATTTTAGACCTGTCTTAGTCGTGGTAGCCCAACTTTTGCCTATGTCCGGTGTACGCACACGACTACCCCGAGTCCTCTCCGGAGTAAACTTACCCATATCACGCAGCGTGGGAATCCCTCCACCTCCCTTAAGACCCAATGATTTCCCAAAGGCGCCACGCCGAGAGTGAGAACGTGCCTCTGTTCAACCCTCTTTCAGTCCGCATATGGTTGTGTCGGGGGCCTCGCATTGACCTGCAATGGCGCCACGCTCAAACGCCCCGTCTACGTTCTACGGTTCTTAAACAAAGGAAGATGGCCAATTAGCAATTTGCAAACCCTGTATCAGTTCAGCTGGGGAGTTCGCCATGCAGTGAGTCTTGAGTCTGTTTAGAAGGCCAGGTTCTAGTGAAGTGGTCCATCGCCTGGGCTGTAAATGATTGTCCGAAATCTGATTACGACGGCCGTCGAATTAATAACTGTACTCAGCAACAAAGAATGAGTACATAGACGTATTTGAAAGTGATAACTGAACAGGCAATGCTGCAAGACTAAATATTTTGATTTCCCGCAATAACTGGTATGCATCGGGGTAAAAGCAAGATCATTGTCCAAGCGCTCCACAAACCAGTTAGTTCTAACGATGCTAGACGGGTCTTACCGCCACGAATGTTATCCGACTCCCAGCCCCACCCTAGGTCTTTAGGCCACTACACCCTAGTGATGAGTGCCGCTACCGCACACGGTGCCTAATGCTGGCCATTTCGGCGTAGGGGTCAATTGAGCACGAAGAGGATTCTGGGATGTAGTTGATACCTCCTCATGCGATCCGTCTCAGAAGTATGTTCAAGGACAGGCCCCACGATTTGGAGGACGGAGTAGGGTAGCACTCGTGACGACATTTAACAATTTTACCAAACGACCCATCTCTGTTTATGCTGAGGAATGACGTTCTGAGATACTCCTCCATGCTAATATTAATAGAAGGTACTATTTTATAACCCAACAGCTACCCTTGGCGTAGATGCTGCGCACGAATGTTATCCGACTCCATCTTACAACTTCGCCACCTAATCACTGACTGTGGGATGTATCGGCCGGTAACAGCTTGGGATGGCGTAGGATAGCACTCGTGGTTCACAGTAGCATCACCGCTAAAGCTCCCAGCGATCGGCCTCGTTATAAGGGCAGATATCATTACCTCTGTCGAAGATCGCGACACGCAATATGAGGTCATTTGGGTCTGATTGTGTGTATCGATCATGTTTTACTCGGCTACGCGAAGTTATAACCACAGCCTAACGTGCTACTTACCTCCCCTGTACCGTTCTCCGCTCCTATTTTAATAGGGGATCCAATGCGGGATGATCATGGGGATAAATTTTTTGCGGGTCGATGGGTAGTTTTTTGTTGTCCTTTAAGGCAGTGGGGTTGGGAACGCTGCAAAACTACACCTCTGCTCATCACGGTTTAAAGCGGCAGCCACACGTCCCACCCAGTTGATTGCCGAGTCTCTCTATTGGCGTCCGCGCTGAGTTGTTAATGCTCTGTAGGACAGCACCGCGAGTTTCGATATCGGTTTACAGATGAGATGGTGGATGGACTTAAGGCGCTATGGCAGGTCGGGTGCTCTACGTACAGGGTGCAGAGTGAAAAGGTCAGTTTCATTGGAACATTCCCCTTGTATGACCCTGTCAGGGGCGGGCCCTATCGATAGGGTTATAGAAGTGCTTCGGCGTGCAGGTCCTTCCTGTTGGTAATCGTACTGTCTCGGACGCCTCGACGAAAAGTTAGGCACGAATGCTACCCGACCCCCTCCAGGGGTCGGGTAGCATTCATGCATTAACCGTCAAATGTAGAGACAGGTGCCTGTGGGACCAATGTGTAATCTGTGACCTTCTTCTTTACTTGGCATCCCGAGCTTTACCACGGATCCCTGCTAGCGAAACAAACAATGTCTCTATAGATATATTAGCTATGGTGCGCGGTGAAGATTGCGTAAGTACACGGGCCAACCATATCCTAGACACGATGACAAGATTATACAATGCCTATCGGAGAACCTAGACATAGCGGTTTTTGACAACGAATTCTCGCGCAGACCGTGTTTTCCTATGATCAAAGGGAGTATTTGCAGTCTAAACGCTCAGTTACCTTTTGATGCTGTCGCACGTCTGTGTGTAGTAATTGGTTGCTTACACGTGCTATGATCTCGGGAAGTTTGGAGCATTACAGGAACCACATCGCGGAGAGTTTCTGTCTGGGAGGCGTTCTGCATAACCCGATCGTATTCGTGCCCTGCATTTGCAACTGAAAGGAAGCACCTCTACAACGCCTAGTACTACGAGAGCCAGCTATAGCTCTCATATATTCCGACACTTCGGTTAACGTTTAGAGATCTCCTCCACACAGGATTTACGATTCGGTCTTTCGTAGTGATGGGCCCGTGTATACCATCGATAGAAGGCTTTACTTCTTTACCCGAGTTAGGCTCGCAGCCTGACGCTTGTCGACCAGCAACCACCTTGAACTCGTCCTCCATAGCGACCGCGTGACAACCGACCCCGAACAATCGCCCGAGCCGCACCCAACTTGGTGATCGATGGTGTTGGGTAACATTCGTGCAACTGGGTGTTGGGTAGCATTCATGCTTTCGTGGATCGCGTAAGTCATGAAGCGATCTTGAGAGCGACGCCAAACGAGCCCTGCCTTTTGCACGAATGCTATCCGACACCCTCACAAACCCCGTATGCGCTTTAAATTTCCTTAATTTCTTGGGTAAAGCTTTATCGCTGATATTAAGCTAGATGAATTATGCAACAAGTCTCGTTCCAAGACGATATACTAAGCACAGTTGCTCGGTAGATGCATATCGATACACTTCGGTAGGTTAAGCTCGGACATGGACCCCCCGGTCAGCCAGCCTCATAGTAATTTACCCGTATGAAACGATGGGAGGATGAGAGAAGAATTAACAGATAACTTTATATTACAGAATTAACGCTACCCGACTCTAAAAGGCATGTGTTGATGCAGTCTCTCATCTATAGCGAGGCACCGTGACTCATGGTTCCAAAGACAATGGAGACTTGTCGTTCCGCCTAACGCACCGTTCTTGATGTCCTTTTGCTAATCTCACGCACGCAAACTAGAACTGGCTACAGGATTGGTGCGTGAGGGCTGCCTAGCTGGATGCTTCAAGGAACATATGACGTCGATACCACTTCGTAGTACGTTTGAACAATGGAGGCACCGCAGACAATTCCACTTGCTGACAGATCTCCTCTTAAGTGAATAGTACGAATCAGGGATTCATTCGTGTCCGGATAATCCCCTTTAAGCGTGAGTGAAATCTGACCGACAATTAACCTGTGGAAACTCAGAAGGATTCGAAATCATTTTGAGTCCCCACTAGTTGCACGTCGACTGGTCAGCTGGATCCGAAGATCAGGCACCACTCAAGCACGAGCGTGCTAGCAGATATCTCCCGGAGTAAATTAACTATTCCCTCGATTAACTGACCGTCGCAGCGGTTATCTGCAGAGCCATGAGTGCTATCCGACTCCCTCATAAAGCTCCAGTTACGAGAGGGCAACTAACGGGGGCCCTAATCGCGTACCATTTGCCGAGTGTCTAGGGGCAATAGCGTCCGGCTCATAAACTGCAATCCTCTCTAGAGTTGACATCAGCTCGACCAGCTGGCAACGTGGGTCGTTACCTTCCATTCATGGGACGGAGGGTGGTATCACGTCTACGGCCTATTGAGCGCTCCATCTACCATCTCCAGACCGCCTATTCTGACATGTGGCCTAATTCGTCTCAATTCGCGGAGCGACGCGAAGAAAAGCATCAATGATTATGGTGGGAGACCGTTATATCGGTGGGACTTGCTGTGCCATACAGATTGGCCTAGGCTACATCAACCGTGCTCGTTTTTTAAGTCGCTCTGGAGTACCGTCAGAACGGATGACTGGCTGGAATCGTTCTAGTTTATAACGGCTTTAGCTGACGTTAATCCGCAGTGGCTAGGGGTCGGGTAGCACTCATGGTAGGGCGTGAACGCATGCATTTCACTACTTTGGGCATTTCGAGGAATCAGTAAGATTAAAAGCAATCCCCTTGGAGATAATGGCCGTGAGTGACTGCGGCTATGTTTGACAGGTTGATAAGCATTCAGGATGACATGATTAAGACACGAGCGTAAGTCAAAGCAAAGTCTTGTGCAGATGTGCAGTAGTTTGAGGGTTCCCGATAGGCGCCCTAAACCTAGTTTTGGGTACAAGTTTCGGGGCCAGTCGGTCCTGTAACGCGTAGCAGTGGACAGGGTGAATGCCGACCCTACGGAAAAGAGTTCAAACCAGGCATTTAGCGAAACAAGAATGAGTATGA"
AA_seq = "HECYPTPS"


def peptide_encoding(seq, AA_seq):
    f = open("codon_table.txt", "r") ##generates the codon list
    codon_dict = {}
    for i in f.readlines():
        codon_dict.update({i[:3]: i[4]})

    seqList = []
    for i in range(len(seq)-len(AA_seq)*3):
        AAList = []
        nucList = []
        workingSeq1 = seq[i:i+len(AA_seq)*3].replace("T", "U")

        for k in range(len(workingSeq1)):
            if k%3 == 0:
                nucs = workingSeq1[k:k+3]
                nucList.append(nucs)
                
        for j in nucList:
            AAList.append(codon_dict[j])
        
        if "".join(AAList) == AA_seq:
            print "match @",i
            seqList.append(workingSeq1.replace("U", "T"))

            ##below handles the reverse_comp
        nucList = [] ##needs to clear the list
        AAList = []
        
        rev_comp = []
        for x in workingSeq1:
            if x == "A":
                rev_comp.append("U")
            elif x == "U":
                rev_comp.append("A")
            elif x == "C":
                rev_comp.append("G")
            elif x == "G":
                rev_comp.append("C")
        rev_comp = "".join(rev_comp)[::-1]
        #print rev_comp, workingSeq1, i

        for y in range(len(rev_comp)):
            if y%3 == 0:
                nucs = rev_comp[y:y+3]
                nucList.append(nucs)
                
        for z in nucList:
            AAList.append(codon_dict[z])
            #print AAList
        
        if "".join(AAList) == AA_seq:
            print "match at rev comp", rev_comp, workingSeq1
            seqList.append(workingSeq1.replace("U", "T"))
        

    return " ".join(seqList)

print peptide_encoding(sequence, AA_seq)
                    

        
