#!/usr/bin/python

# In this exercise I have to filter a list of accessions and print only those that
# satisfy certain criteria

# Importing the re module
import re

# The accession list
acc_list = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

# Printing only those containing the number 5
print("########## " +
      "Accessions containing the number 5 " +
      "##########")
for acc in acc_list:
    if re.search(r'5', acc):
        print(acc)


# Printing only those containing the letter e or d
print("########## " +
      "Accessions containing the letter e or d " +
      "##########")
for acc in acc_list:
    if re.search(r'[ed]', acc):
        print(acc)


# Printing only those containing the letters d and e in that order
print("########## " +
      "Accessions containing the letters d and e in that order " +
      "##########")
for acc in acc_list:
    if re.search(r'd*e', acc):
        print(acc)



# Printing those containing the letters d and e in that order with one letter in between
print("########## " +
      "Accessions containing the letters d and e in that order, with one letter in between " +
      "##########")
for acc in acc_list:
    if re.search(r'd.e', acc):
        print(acc)


# Printing those containing the letters d and e in any order
print("########## " +
      "Accessions containing the letter d and e in any order " +
      "##########")
for acc in acc_list:
    if re.search(r'(d*e)',acc) or re.search(r'e*d', acc):
        print(acc)


# Printing those starting with x or y
print("########## " +
      "Accessions starting with x or y " +
      "##########")
for acc in acc_list:
    if re.search(r'^[xy]',acc):
        print(acc)


# Printing those starting with xy and ending with e
print("########## " +
      "Accessions starting with x or y and ending with e " +
      "##########")
for acc in acc_list :
    if re.search(r'(^[xy].+e$)', acc) :
        print(acc)


# Printing those containing any three numbers in any order
print("########## " +
      "Accessions containing any three number in any order " +
      "##########")
for acc in acc_list:
    if len(re.findall(r'\d', acc)) == 3:
        print(acc)


# Printing those containing three different numbers
print("########## " +
      "Accessions containing three different numbers " +
      "##########")
for acc in acc_list:
    match = re.findall(r'\d', acc)
    numbers = set(match)
    if len(numbers) == 3:
        print(acc)


# Printing those containing three or more numbers in a row
print("########## " +
      "Accessions containing three or more numbers in a row " +
      "##########")
for acc in acc_list:
    if re.search(r'\d{3,}', acc):
        print(acc)


# Printing those ending with d, followed by either a, r or p
print("########## " +
      "Accessions ending with d followerd by either a, r or p " +
      "##########")
for acc in acc_list:
    if re.search('d[arp]$', acc):
        print(acc)
