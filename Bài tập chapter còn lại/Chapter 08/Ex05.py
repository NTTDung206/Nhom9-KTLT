# Exercise 5: 
filename = input("Enter a file name: ")
count = 0

fhand = open(filename, 'r')
for line in fhand:
    if line.startswith('From:'):
        print(line.split(' ')[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")