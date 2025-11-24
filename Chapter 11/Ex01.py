# Exercise 1: 

import re # 

filename = input("Enter the filename: ")
regex = input("Enter a regular expression: ")

counter = 0
fhand = open(filename, 'r')
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        counter += 1

print(counter)