# Exercise 4: 

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
email_addresses = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1

max_address = None
max_emails = 0
for k in email_addresses:
    if email_addresses[k] > max_emails:
        max_address = k
        max_emails = email_addresses[k]

print(max_address, max_emails)
