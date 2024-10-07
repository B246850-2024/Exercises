#!/bin/bash
# This script reads the data from example_people_data.tsv;
# Extracts the country collumn and gives each line an index number.

IFS=$'\t'

count=0
while read name email city birthday_day birthday_month birthday_year country
do
echo -e "${count}\t${country}"
count=$(( ${count} + 1 ))
done < example_people_data.tsv
