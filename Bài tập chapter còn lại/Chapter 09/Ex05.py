# Exercise 5: 

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
domains = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        domain = email.split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)