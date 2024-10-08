#!/bin/bash
# This script reads the data from example_people_data.tsv;
# Extracts the name, city, country collumns and gives each line an index number.
# It has two outputs: the first output is printed on the screen and flags the empty and header lines.
# The second output is a "cleaned" version of output 1, without the empty and header lines, and its saved in the index_other_info.out file

IFS=$'\t'

count=0
while read name email city birthday_day birthday_month birthday_year country
do
	if [ -z $name ]; then
	echo "Empty line"
	
	elif [ $name != "name" ]; then
echo -e "${count}\t${name}\t${city}\t${country}"
echo -e "${count}\t${name}\t${city}\t${country}" >> index_other_info.out

count=$(( ${count} + 1 ))

	else
	echo "Header line"

	fi

done < example_people_data.tsv
