#!/usr/bin/python

#This script counts the number of A and T a sequence
#It also tells you how much of the sequence is composed by A or T

#Preparing library
import os, sys

# Saving the sequence file name into a variable
DNA_seq_file = sys.argv[1]

# Reading the sequence file
DNA_seq = open(DNA_seq_file).read().rstrip("\n")
DNA_seq = DNA_seq.upper()

# Checking if a DNA sequence containing only A, T, C, and Gs was provided
sorted_bases = sorted(set(DNA_seq)) # getting the unique characters and sorting them
joined_bases = ''.join(sorted_bases) # joining the bases into a string

if "ACGT" == joined_bases:
    print("This looks like a DNA sequence")
else:
    raise ValueError("Error: This is not a DNA sequence!\nIt must have only A, T, C and G")

# Counting the number of Ts and As

Ts = DNA_seq.count("T")
As = DNA_seq.count("A")

print("There are ", Ts, " Ts and ", As, " As in this sequence")

# Getting the percentage of the sequence that is composed by Ts and As
perc = (Ts + As)/len(DNA_seq)

print(perc, " of this sequence is made up of As and Ts")
