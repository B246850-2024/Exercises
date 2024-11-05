#!/usr/bin/python

######################  Function that count the kmers appearing more than n times ##############################

# The kmers are built with an offset of 1

def kmers(sequence, kmer_size = ["2"], min_freq = 2) :
    sequence = sequence.upper()
    length_sequence = len(sequence)
    kmers = [] # empty list were the kmers will be stored
    
    # Loop over the k sizes provided and get the kmers for that k
    for k in kmer_size :
        k = int(k)
        position = 0
        while (position < (length_sequence - k + 1)):
            kmers.append(sequence[0 + position : k + position])
            position +=1

    uniq_kmers = list(set(kmers)) # list of unique kmers
  
  # print("List of unique kmers in the sequence", uniq_kmers)
    
    min_freq_kmers = [] # empty list where the kmers with the mininum frequency provided are stored
    
    # Loop over the unique kmer list, count how many times each of those appear in the kmer list
    # Those with frequence higher then the minimun are stores in the min_freq_kmers
    for k in uniq_kmers:
        freq = kmers.count(k)
        if freq > min_freq :
            min_freq_kmers.append(k)
    
    # Sorting the selected kmers by size, and then alphabetically
    min_freq_kmers = sorted (min_freq_kmers, key=lambda x: (len(x), x))

    k_string = ", ".join(kmer_size) # joining the k values into a string so they can be printed with the output message

    # Output message
    print("############\n", k_string, "-mers that appear at least ", min_freq, " times in the sequence:\n", min_freq_kmers, "\n##############")

    return min_freq_kmers # returning the output (a sorted list of kmers)



###################################### Testing the code on Arabidopsis thaliana rbcL gene #########################################

# Reading the fasta file, striping out the header, and saving it to a variable called dna
dna = ""
with open("arabidopsis_rbcl.fasta") as my_file :
    for eachline in my_file:
        eachline = eachline.rstrip("\n").upper()
        if (eachline.startswith(">")) :
            print("Skipping the fasta header file")
        else :
            dna = dna + eachline

# Setting the parameters
kmer_sizes = ["2", "3", "4"] # kmer sizes
min_freq = 30 # minimun frequence

# Testing the code on the sequence.
kmers(dna, kmer_sizes, min_freq)
