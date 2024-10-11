#!/bin/sh

# Script to "fix" the fasta files imported from NCBI, which have a empty line between each sequence

rm -f fixed_mock_NCBI.fasta

while read -r line; do

    if [ -z "$line" ]; then
        echo "Empty line removed"

    elif [ "$(echo "$line" | cut -c1)" = ">" ]; then
        echo "$line" >> fixed_mock_NCBI.fasta

    else
        echo "$line" > temp.txt
       	sed -i 's/a/A/g' temp.txt	
       	sed -i 's/t/T/g' temp.txt	
       	sed -i 's/c/C/g' temp.txt	
       	sed -i 's/g/G/g' temp.txt	
	cat temp.txt >> fixed_mock_NCBI.fasta

    fi

done < "$1"

rm -f temp.txt
