filename = input("Enter a file name: ")
with open(filename, "r") as file:
    for line in file:
        print(line.strip().upper())