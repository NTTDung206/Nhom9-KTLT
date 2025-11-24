filename = input("Enter the file name:")

if filename.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    with open(filename, "r") as file:
        count = 0
        for line in file:
            if line.startswith("Subject:"):
                count = count + 1
        print("There were", count, "subject lines in", filename)
except FileNotFoundError:
    print("File cannot be opened:", filename)