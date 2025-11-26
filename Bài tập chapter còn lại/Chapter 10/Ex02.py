# Exercise 2: 

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
hours_of_day = {}

for line in fhand:
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(":")[0]
        hours_of_day[hour] = hours_of_day.get(hour, 0) + 1

lst = list(hours_of_day.items())
lst.sort()
for t in lst:
    print(t[0], t[1])