#!/usr/bin/python

# Printing the gene names for D. melanogaster and D. simulans
with open("data.csv") as my_file :
    print("###########\nGene names for D. melanogaster and D. simulans\n############")
    for eachline in my_file :
       line_list = eachline.split(",")
       if (line_list[0] == "Drosophila melanogaster") :
           print("D. melanogaster: ", line_list[2])
       elif (line_list[0] == "Drosophila simulans") :
           print("D. simulans: ", line_list[2])
    print("\n")

# Printing the name of genes with length between 90 and 110 bp.
with open("data.csv") as my_file :
    print("###########\nGene names for genes with 110 < lenght >90\n############")
    for eachline in my_file :
        line_list = eachline.split(",")
        gene_length = len(line_list[1])
        if (gene_length >= 90 and gene_length <=110) :
            print(line_list[2], " has a lenght of ", gene_length, "bp")
    print("\n")

# Printing the names of genes with AT content < 0.5 and expression level > 200
with open("data.csv") as my_file:
    print("###########\nGenes with AT content < 0.5 and expression level > 200\n############")
    for eachline in my_file :
        line_list = eachline.rstrip("\n").split(",")
        gene_length = len(line_list[1])
        a_content = line_list[1].upper().count("A")
        t_content = line_list[1].upper().count("T")
        at_content = (a_content + t_content) / gene_length
        if (at_content < 0.5 and int(line_list[3]) > 200) :
            print(line_list[2])

# Printing the names of genes starting with "k" or "h", except for those belonging to D. melanogaster
with open("data.csv") as my_file :
    print("###########\nGenes with AT content < 0.5 and expression level > 200\n############")
    for eachline in my_file :
        line_list = eachline.rstrip("\n").split(",")
        if (line_list[0] != "Drosophila melanogaster" and (line_list[2].startswith("k") or line_list[2].startswith("h"))) :
            print(line_list[2])

# For each gene, printing the name and a message saying whether its AT content is high (>.65), medium (.45<>.65) or low (<.45)
with open("data.csv") as my_file :
    print("###########\nGenes with AT content < 0.5 and expression level > 200\n############")
    for eachline in my_file:
        line_list = eachline.rstrip("\n").split(",")
        gene_length = len(line_list[1])
        a_content = line_list[1].upper().count("A")
        t_content = line_list[1].upper().count("T")
        at_content = (a_content + t_content) / gene_length
        if (at_content > 0.65) :
            print(line_list[2], " gene has a high AT content (", round(at_content, 2), ")")
        elif (at_content < 0.65 and at_content > 0.45) :
            print(line_list[2], " gene has a medium AT content (", round(at_content, 2), ")")
        elif (at_content < 0.45) :
            print(line_list[2], " gene has a low AT content (", round(at_content, 2), ")")

