#!/usr/bin/python


## Amino acid percentages, part two
print("Second version of the amino acid percentage script:\n")

def amino_percent(sequence, residue = ["A", "I", "L", "M", "F", "W", "Y", "V"]) :
    length = len(sequence)
    percents = 0
    for aa in residue :
        amino_count = sequence.upper().count(aa.upper())
        print("The amino acid residue ", aa, " occurs ", amino_count, " times in this sequence")
        percentage = round(((amino_count / length) * 100), 2)
        print("This corresponds to ", percentage, "% of the whole sequence")
        percents = percentage + percents
    print("All these residues combined ammount to ", percents, "% of the whole sequence") 
    return percents

# Human histone sequence (accession AAC61625.1 on NCBI)
aa_sequence = "maggkagkdsgkaktkavsrsqraglqfpvgrihrhlksrttshgrvgataavysaaileyltaevlelagnaskdlkvkritprhlqlairgdeeldslikatiagggviphihksligkkgqqktv"

# The percentage of hydrophobic amino acids in the sequence
output = amino_percent(aa_sequence)
print("\nThis is the output of the function:\n Just the percentages summed:\n", output)

assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(amino_percent("MSRSLLLRFLLFLLLLPPLP")) == 65
