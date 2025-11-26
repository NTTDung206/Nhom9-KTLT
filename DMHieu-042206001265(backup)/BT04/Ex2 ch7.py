filename = input("Enter the file name:")
with open(filename, "r") as file:
    count = 0
    total = 0.0

    for line in file:
        line = line.strip()

        if line.startswith("X-DSPAM-Confidence:"):
            number_str = line.split(":")[1].strip()
            number = float(number_str)
            total += number
            count += 1

    if count > 0:
        avarage = total / count
        print("Average spam confidence:", avarage)
    else:
        print("NOT FOUND")