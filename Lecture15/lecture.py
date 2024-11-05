#!/usr/bin/python

# Getting the AT content of a sequence

my_dna = "actgatacatatatatcgatgcgttcat"

length = len(my_dna)

a_count = my_dna.upper().count('A')
t_count = my_dna.upper().count('T')

at_content = (a_count + t_count)/length

print("AT content of ", my_dna, "is ", round(at_content, 2))


## We can write a function to do that for us for any given sequence

def get_at_content(some_dna) :
    length = len(some_dna)
    a_count = some_dna.upper().count('A')
    t_count = some_dna.upper().count('T')
    at_content = (a_count + t_count) / length
    print("Using a function:\n The AT content of this sequence is ", round(at_content, 2))
    return at_content

get_at_content(my_dna)


## All variables defined within a function exist only within that scope. If you try to call them
## outside the function you'll get a NameError saying that variable is not defined.

## You can make several return lines in the function, but the first return line the function sees will
## act like a break command, stoping the function and returning the stated output.

## Do not rely on variables defined outside the function to write it. It will work, but the function will not be self-contained.

## If any one else tries to use it, they will fail because they do not have that variable defined.

## Make sure you use the return command, and not only a print command. Otherwise the function's output cannot be saved into a variable.


## Making the round command a argument of the function

def get_at_content(some_dna, decimal_places) :
    length = len(some_dna)
    a_count = some_dna.upper().count('A')
    t_count = some_dna.upper().count('T')
    at_content = (a_count + t_count) / length
    output = round(at_content, decimal_places)
    print("This is the AT content with a precision of ", decimal_places, " decimal places: ", output)
    return output

get_at_content(my_dna, 3)


## Adding 2 decimal places as the default

def get_at_content(some_dna, decimal_places = 2) :
    length = len(some_dna)
    a_count = some_dna.upper().count('A')
    t_count = some_dna.upper().count('T')
    at_content = (a_count + t_count) / length
    output = round(at_content, decimal_places)
    print("This is the AT content with a precision of ", decimal_places, " decimal places: ", output)
    return output

get_at_content(my_dna)



## We can test a function using the assert command. You tell it the function, the arguments and the expected ouput. If the function returns the right output, you get nothing back. But if it is different it will give you a AssertionError back.

## Assertions work as checkpoints that tell if the function is working properly.

## Python3 can make slight rounding errors when working with floating point numbers, specially when there are many decimal places. Using the round function before the assertion in those cases is a good idea.
