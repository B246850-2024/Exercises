#!/usr/bin/python

# This script does an in-silico double digestion of a DNA sequence
# with two different fake restriction  enzymes Bpsml (ANT*AAT)
# and Bpsmll (GCRW*TG).

# I thought about two ways of doing this:
# 1) Use re.finditer() to find all restriction site, and then use their positions to slice the string.

# 2) Use re.split() to generate the fragments, but the will miss the restriction site bases, so these
# would have to be added again

# Library
import re

with open("long_dna.txt")  as my_file:
    dna = my_file.read().rstrip()
    print("######### " +
            "This is the DNA sequence to be digested " +
          "########")
    print(dna)

# Fragment lenghts when cutting with Bpsml
sites_I = re.finditer(r'A[ATCG]TAAT', dna)
print(sites_I)
# Maybe I can do something like this, looping over the re.finditer object (here caled sites)
start = 0
fragments_I = []
for site in sites_I:
    end = site.start() + 3  # dont know yet if 3 or 4, I have to think carefully about the python indexing
    # This will be the end of the first fragment
    fragment = dna[start:end] # Slicing the string
    fragments_I.append(fragment) # Saving the slice (aka the fragment)
    start = end # reseting the end point of fragment a to be the starting point of fragment b
                # quite philosophical if you ask me

# This loop gets all but the last fragment
# Getting the last fragment
fragments_I.append(dna[start:])


# Getting the length of the fragments
print("############ " +
        "Length of the fragments cut with Bpsml "
      "############")
counter = 0
for fragment in fragments_I:
    counter += 1
    frag_len = len(fragment)
    print("The fragment number " + str(counter) + " has a length of " + str(frag_len))



# Now lets digest these fragments using the enzime Bpsmll to generate
# the double digest process
fragments_II = []

for fragment in fragments_I:
    sites_II = re.finditer(r'GC[AG][AT]TG', fragment)
    start = 0
    for site in sites_II:
        end = site.start() + 4
        fragments_II.append(fragment[start:end])
        start = end
    fragments_II.append(fragment[start:])



# Getting the fragment length
print("############ " +
        "Length of the fragments cut with Bpsml and Bpsmll "
      "############")
counter = 0
for fragment in fragments_II:
    counter =+ 1
    frag_len = len(fragment)
    print("The fragment number " + str(counter) + "has a length of " + str(frag_len))



# Printing the fragments
print("########## " +
        "Fragments of the double digestion " +
      "#########")
for fragment in fragments_II:
    print("\n" + fragment)
