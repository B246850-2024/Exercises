#!/usr/bin/python

# This script gives you the complement of a DNA sequence

#Preparing library
import os, sys

# Saving the sequence file name into a variable
DNA_seq_file = sys.argv[1]

# Reading the sequence file
DNA_seq = open(DNA_seq_file).read().rstrip("\n")

# Checking if it is a DNA sequence
sorted_bases = sorted(set(DNA_seq))
joined_bases =''.join(sorted_bases).upper()

if joined_bases == "ACGT":
    print("This looks like a DNA sequence")

else:
    raise ValueError("Error: This is not a DNA sequence!\nIt most have only As, Ts, Cs, and Gs")

# Getting the complement sequence
DNA_seq1 = DNA_seq.replace("T", "a")  # Replace T for A
DNA_seq2 = DNA_seq1.replace("A", "t") # Replace A for T
DNA_seq3 = DNA_seq2.replace("C", "g") # Replace C for G
DNA_seq4 = DNA_seq3.replace("G", "c") # Replace G for C
DNA_seq5 = DNA_seq4.upper() # Makes it all upper case again

print("This is the original sequence: ", DNA_seq)
print("This is the complement of  it: ", DNA_seq5)
