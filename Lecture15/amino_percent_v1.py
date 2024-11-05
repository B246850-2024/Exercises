#!/usr/bin/python


## Amino acid percentages, part one
print("First version of the amino acid percentage script:\n")

def amino_percent(sequence, residue) :
    length = len(sequence)
    residue = str(residue).upper()
    amino_count = sequence.upper().count(residue)
    print("The amino acid residue ", residue, " occurs ", amino_count, " times in this sequence")
    percentage = round(((amino_count / length) * 100), 2)
    print("This corresponds to ", percentage, "% of the whole sequence\n")
    return percentage

# Human histone sequence (accession AAC61625.1 on NCBI)
aa_sequence = "maggkagkdsgkaktkavsrsqraglqfpvgrihrhlksrttshgrvgataavysaaileyltaevlelagnaskdlkvkritprhlqlairgdeeldslikatiagggviphihksligkkgqqktv"

# The percentage of alanine in this sequence
amino_percent(aa_sequence, "a")


## Testing the function with assertions
assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

