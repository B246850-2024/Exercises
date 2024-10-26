#!/usr/bin/python
# This program gives some information on the splicing of a DNA sequence
# The inputs are:
#   1) The file name where the sequence is kept;
#   2) The starting and ending positions of each intron, in order;

# It can only work with sequences that have only one intron

# The outputs are:
#   1) The coding sequence;
#   2) The percentage of the sequence that codes for something;
#   3) The whole sequence with exons in upper case and introns in lower case

# Preparing the library
import sys

# Getting the sequence file name
DNA_seq_file = sys.argv[1]

# Saving the sequence into a variable
DNA_seq = open(DNA_seq_file).read().rstrip("\n")

# Checking whether the fisrt input is actually a sequence
sorted_bases = sorted(set(DNA_seq))
joined_bases = ''.join(sorted_bases).upper()

if joined_bases == "ACGT":
    print("### This looks like a DNA sequence ###")
else:
    raise ValueError("Error: This is not a DNA sequence!\n It must have only As, Ts, Cs, and Gs")

# Importing the intron starting and end positions
intron_start = int(sys.argv[2]) - 1 
intron_end = int(sys.argv[3])

#print(intron_start, "\n", intron_end)

# Getting the coding sequence by removing the introns
exon1 = DNA_seq[0:intron_start]
exon2 = DNA_seq[intron_end:]
exon = exon1 + exon2

print("### The coding sequence ###\n", exon)

# How much of the sequence is actually coding for something
perc_seq = round((len(exon) / len(DNA_seq)) * 100, 2)

print("### % of this sequence that is coding ###:\n", perc_seq)

# Whole sequence with exons uppercase and introns lowercase
intron = DNA_seq[intron_start:intron_end].lower()

seq_case = exon1 + intron + exon2

print("### The whole sequence, with exons in upper case and introns in lower case ###\n", seq_case)

