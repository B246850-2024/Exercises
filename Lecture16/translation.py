#!/usr/bin/python

# Importing library

# This script reads a DNA fasta file and translates it into protein
# The DNA file must be in the same folder as the script and be called dnaseq.fasta

# The main object is a function that translates the DNA

# This function will only accept A,C,T,G and N as bases

# Creating a dict to represent the genetic code
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# Reading the DNA file
with open("dnaseq.fasta") as my_file:
    dnaseq = ""
    for eachline in my_file:
        if eachline.startswith(">"):
            print("\nReading the fasta file with header:\n", eachline)
            print("\nSkipping header line in fasta file")
        else:
            readline = eachline.upper().rstrip("\n")
            dnaseq = dnaseq + readline
    print("##############\nThis is the DNA sequence:\n", dnaseq,"\n################")


# translation function
def translation (seq, frame = 1, coding_reg = []):
    
    # Stablishing the coding sequence
    # If the user does not provide a value, the default is adopted (i.e., the whole sequence)
    if coding_reg == []: # user did not provide value
        coding_reg = [1, len(seq)]
    else:
        coding_reg = coding_reg # user provided value
    
    # Defining a few key variables
    ptn = ""
    position = 0
    accepted_bases = {'A', 'T', 'G', 'C', 'N'}
    start = coding_reg[0] - 1 # taking 1 from the index because Python starts at 0
    end = coding_reg[1] # adding 1 because Python is non inclusive in the rigth side
    
    # Making sure the DNA bases are uppercase
    seq = seq.upper()
    
    # Slicing the sequence to get the coding part
    coding_seq = seq[start : end]
    print("\n######This is the coding sequence######\n", coding_seq, "\n##########################")
   
    if set(coding_seq).issubset(accepted_bases) : # error trap for unwanted DNA bases
        while position < (len(coding_seq) // 3): # looping over each codon
            codon = coding_seq[0 + (3 * position) : 3 + (3 * position)]
            #print("#######\nThis is the codon:\n", codon, "\n########")
            if "N" in codon: # If the codon has a N, assign a undetermined amino acid X
                aa = "X"
            else: # If it does not, assign it a amino acid according to the genetic code
                aa = gencode.get(codon)
            #print("######\nThis is the amino acid:\n", aa,"\n##########")
            ptn = ptn + aa
            position = position + 1
        print("\n######## This is the protein ################\n", ptn)
        return (ptn)
    else:
        print("Error: Your sequence contains other bases apart from A, T, C, G and N")
        return()

#protein = translation(dnaseq, frame = 1, coding_reg = [174, 731])


# Assert statements
# Assert #1: Translation the small rubisco subunit from Cucumis sativus (NM_001405108.1)
dnaseq1 = "ACGACCACTAAATTGGTTTGTGAATGGATAAAATGAGGATAGTAAACAGCTTATAAATAGACTACCATTTCACAGTGCAATGCCTCTCAGACTCAACACCAAGAGCTTCTTCAAACTACTCTACTAGCTATTAGTAAATCCTTCTAATCCTCCAAGAAAAAAAAGAGGCATAAATGGCTTCATCCATTCTCTCATCCGCCGCTGTTGCCTCTGTGAACAGTGCTTCCCCTGCTCAAGCTAGCATGGTAGCACCATTCACTGGCCTCAAATCTTCCGCTGGTTTCCCCATCACTCGCAAGAACAACGTCGACATCACCACTTTGGCTAGCAATGGTGGAAAAGTTCAGTGCATGAAGGTGTGGCCACCACTTGGATTGAGGAAGTTCGAGACTCTTTCTTACCTGCCTGATATGAGTAACGAACAATTGTCAAAGGAATGTGACTACCTTCTCAGGAATGGATGGGTTCCCTGCGTTGAATTCGACATCGGAAGCGGATTCGTGTACCGTGAGAACCACAGGTCACCAGGATACTACGATGGACGTTACTGGACCATGTGGAAGCTCCCTATGTTTGGCTGCACCGACTCATCTCAGGTGATTCAGGAGATTGAGGAGGCTAAGAAGGAATACCCCGACGCATTCATCAGGGTTATTGGCTTTGACAACGTCCGTCAAGTGCAGTGCATCAGTTTCATCGCCTACAAGCCCCCAAGATTCTACTCTTCTTAAGTTCCATCTGCTGAGGCTTTCTTGAGGCGAATTTCCACCATTTGCCTTTTTTAAAGCTCCATCACTTGGGTGGTTTCAACCAAATTTCCCCCCTTTAATTTTTTTCTTCTCTCTTTTTTTTTCCTTCTTATTTTTCCATTTTACGTTTTGGTTTGTCTGTTGAATCCCACTATGTTTATTTCCCCGACTTTCCAATTCGAATTGGAATAAATGATGCTTTGATTTGTTCTTCAATTATCCTATCAATCAATCGGTCCTGTTTGCATCTTTCCTCATGGAAATTCAATCTATTTCCCTATGAAAATGTTCAATTGGGGTTTGTGTTTGTGTGATGGATATTGATTCGTGGTAACGATAAGGTTTAATCAATTTCATCCACTCAACCGTTGTCTTCATTATTCCCTTTTAAATTC"

ptn1 = "MASSILSSAAVASVNSASPAQASMVAPFTGLKSSAGFPITRKNNVDITTLASNGGKVQCMKVWPPLGLRKFETLSYLPDMSNEQLSKECDYLLRNGWVPCVEFDIGSGFVYRENHRSPGYYDGRYWTMWKLPMFGCTDSSQVIQEIEEAKKEYPDAFIRVIGFDNVRQVQCISFIAYKPPRFYSS_"

#assert translation(dnaseq1, frame = 1, coding_reg = [174, 731]) == ptn1
