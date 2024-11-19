#!/usr/bin/python

# Regular expressions (regex) are a sequence of characters that defines a search pattern

# It is kind of a mini language used to find or find&replace patterns in strings

# This same 'language' is used elsewhere like in the grep syntax

# We were using the .find() method to find particular string patterns
sequence = "AATCGCT"
pattern = "TC"
print("The pattern", pattern, "is present at least once, at position", sequence.find("T"))

# The ouput of the method was the positon of the first substring matching the searching pattern.


# To use regex we need to import the module named "re"
import re


# Using the module
print(re.search('a', 'abc'))

# This output is a bit weird when compared to .find()

if re.search('a', 'abc'):
    print("Found and a in the string")
else:
    print("No a found in the string")

if re.search('z', 'abc'):
    print("Found a z in the string")
else:
    print("No z found in the string")

# This seems to work like a TRUE or FALSE output, but actually, but that is not the case

# The types of the two outputs of re.search are not actually 'bool', but 're.Match' when the match
# is successful and 'NoneType' and its unsucessful.

output1 = type(re.search('a', 'abc'))
print("When the match is successful, the object type returned is", output1)

output2 = type(re.search('z', 'abc'))
print("When the match is unsuccessful, the object type returned is", output2)



# One important object when thinking about regex are the raw strings

# Raw strings are a way of telling python to ignore (skip) special characters and interprete them literally

# Raw strings are generated simply by adding and r in front of a string when doing the variable assignment

notraw = '\nraw\nstring\n'
raw   = r'\nraw\nstring\n'

print("\nThis is a string that was not set to raw:\n", notraw)
print("\nThis is a string that was set to raw:\n", raw)


# The syntax of re.search is re.search(pattern, string)

# If we want to search for similar, but distinct patterns, we can allow variation
# in a given character:

dnaseq = "AATTGGCACGATC"
if re.search(r'GG(C|T)AC', dnaseq) :
    print("\nFound the restriction site GG-CorT-AC")
else:
    print("\nRestriction site not found")

# We may enclose as many options in the brackets, separated by the pipe, as we want to

# It is good practice to use the r in front of the searching pattern

# We may also enclose the alternatives with square brackets with no pipe between then

dnaseq = "AGGCCATCGTACT"
if re.search(r'CAT[ATGC]G', dnaseq):
    print("\nPattern found")
else:
    print('\nPattern not found')

# Sometimes it is easier to say what we are NOT looking for

# In the re module this is done by placing a ^ in front of the string

# In the following example we are looking for undetermined bases (not A, C, G or T) in
# the first 6 characters of the string

dnaseq = 'ATWCGGCTAC'
if re.search(r'[^AGCT]', dnaseq):
    print("\nAmbiguous bases in the first six positions")
else:
    print("\nNo ambiguous bases in the first six positions")


# There are tons of different match shortcuts detailed in the website
# Here we will explore some of those

# A full stop (.) matches any character by a new line
dna = "ACCATCA"
match = re.search(r'C.T', dna)
if match:
    print("Match C.T found:\n", match)
else:
    print("Match C.T not found")
# The output tells us the match found and its position in the string


# A question mark means the thing before it is optional
match = re.search("CAAT", dna)
if match:
    print("Match CAAT found:\n", match)
else:
    print("Match CAAT not found")

match = re.search("CAA?T", dna)
if match:
    print("Match CAA?T found:\n", match)
else:
    print("Match CAA?T not found")


# A plus means the thing before can be repeated more than one, but need to be present

# An asterisk is the most flexible, the thing before may be repeated, and it is also optional

# It is also possible to be more specific and search for an specific number of repetitions
match = re.search("AC{1,2}A", dna)
if match:
    print("Match AC{1,2}A found:\n", match)
else:
    print("Match AC{1,2}A  not found")
# In this case we are allowing the C to present once or twice (ACA and ACCA)

# We can check if a string starts of ends with a certain motif by using ^ and $

dna = "ATCGCCGATC"

if re.search(r'^TCG', dna):
    print("\n Starts with TCG")
else:
    print("\nDoes not start with TCG")

if re.search(r'ATC$', dna):
    print("\nEnds with ATC")
else:
    print("\nDoes not end with ATC")


# The true power of regular expresions becomes very clear when we start to combine
# most/all of these features into once search pattern:

# ^G[ATCG]{10,150}ATG[ATGC]{30,1000}TGA[ATGC]{20,50}A{5,10}$

# This expression is looking for a mRNA starting with G, followed by a 5' UTR of 10-150bp,
# then an ATG start codon, followed by a coding region of 30-1000bp, then a TGA stop codon,
# which should then be followed by a 3' UTR of 20-50bp, and finally, the whole thing should
# end on a poly-A tail of 5-10bp.




# re.search function returns a re match object when the match is successful
# There are some methods available to manipulate this kind of object

# For instance, we can call .group() to get the matched substring

dna = "ATCGWACTZ"
match = re.search(r'[^AGCT]', dna)

if match:
    print("\nAmbiguous base found!")
    ambig = match.group()
    print("The ambiguous base was:", ambig)

# As you can see, the ambig variable contains only the W, that is because,
# just like .find(), re.search() only matches the first instance


# Interestingly, we can search for two or more patterns at the same time
# and keep them separately using ()

lots_of_plants = ['Euterpe edulis',
                  'Comanthera centauroides',
                  'Triticum aestivum',
                  'Zea mays',
                  'Oryza sativa',
                  'Ornithogalum adseptentrionesvergentulum',
                  'Totoca']

#for this_plant in lots_of_plants:
#    match = re.search('(.+) (.+)', this_plant)
#    print(this_plant + ': genus is \'' + match.group(1) + '\', specific epithet is \'' + match.group(2) + '\'')


# The last plant name caused problems because its only the genus name
# I have commented it because otherwise it would interrupt the script from running because of the error
# We can add an error trap to deal with that
lots_of_plants = ['Euterpe edulis',
                  'Comanthera centauroides',
                  'Triticum aestivum',
                  'Zea mays',
                  'Oryza sativa',
                  'Ornithogalum adseptentrionesvergentulum',
                  'Totoca']

for this_plant in lots_of_plants:
    match = re.search('(.+) (.+)', this_plant)
    if match:
        print(this_plant + ': genus is \'' + match.group(1) + '\', specific epithet is \'' + match.group(2) + '\'')
    else:
        print("Unable to find genus and specific epithet for the name " + this_plant)

# Notice that we used the values 1 and 2, and not 0 and 1 to extract the matches from the
# match object. That is because the value 0 in this object is actually the whole string
# being inspected, and from 1 onward we have the matches found


# We can also combine a string into our searching pattern

look_for_me = 'AA'

dna = 'GGTACAATCGA'

match = re.search('(.+)' + look_for_me + '(.+)', dna)

print("\nWe found " + match.group(1) +" and " + match.group(2) + " surrounding search string " + look_for_me)

# We can get the position (start and end) of the matched pattern using start() and end()
dna = 'ATCGCGYKNAATTCAC'
match = re.search(r'[^GATC]', dna)

if match:
    print("\nAmbiguous base found!")
    print("The ambiguous base is " + match.group())
    print("It is in Python position " + str(match.start()))


# We can use regex to split strings using re.split()
# This works extactly like split(), but takes regex as input

# Here is a sequence in many ambiguous bases
dna = 'ACTNGCATRGCYTACYGTYACGATSCGAWTCG'

# Lets split it in all places where there is an ambiguous base

splitted_string = re.split('[^ACGT]', dna)

print(splitted_string)



# We can look for multiple instances of the same match pattern using re.findall()

dna = 'ACTGCATTATATCGTACGAAATTATACGCGCG'

print(re.findall(r'[AT]{4,}', dna)) # Looking for all runs of A/T that are at least 4 bases long


# This returns as output a list with all matches, but no further information



# We can find all possible matches and keep each one in a different re match object using re.finditer()

dna = 'ACTGCATTATATCGTACGAAATTATACGCGCG'

match_iter = re.finditer(r'[AT]{3,}', dna)

counter = 0
for match in match_iter:
    counter += 1
    print("Run #" + str(counter) + " is " + match.group() + " and extend from " +
            str(match.start()) + " to " + str(match.end()))



# Finally, we might be interested in considering pattern search with overlap
# For instance, whe might be interested in finding all AorT 3 bases long, allowing overlap

# This is done using the syntax (?=xyz)

stringlength=3
match_overlap = re.finditer(r'(?=[AT]{3,3})', dna)

print(match_overlap)

counter=0
for ATs in match_overlap:
    counter += 1
    run_start = ATs.start()
    run_end = run_start+stringlength
    print('A/T triplet (overlapping): ' +str(counter)+' extends from base ' \
    + str(run_start+1) \
    + ' to base ' +str(run_end)+' and has sequence ' +str(dna[run_start:run_end]))

print('The input sequence was ' + dna)
