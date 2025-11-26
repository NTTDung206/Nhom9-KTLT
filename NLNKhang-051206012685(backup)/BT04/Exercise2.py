import sys

def analyze_spam_confidence():
    while True:
        file_name = input("Enter the file name (e.g., mbox-short.txt): ")
        try:
            file_handle = open(file_name, 'r')
            break
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    total_confidence = 0.0
    count = 0

    for line in file_handle:
        line = line.strip()
        if line.startswith("X-DSPAM-Confidence:"):
            colon_pos = line.find(':')
            try:
                confidence_str = line[colon_pos + 1:].strip()
                confidence_value = float(confidence_str)
                total_confidence += confidence_value
                count += 1
            except ValueError:
                print(f"Warning: Could not convert '{confidence_str}' to float.")
                continue

    file_handle.close()

    if count > 0:
        average_confidence = total_confidence / count
        print("\n--- Results ---")
        print(f"Total lines processed: {count}")
        print(f"Total confidence value: {total_confidence:.4f}")
        print(f"Average spam confidence: {average_confidence:.4f}")
    else:
        print("\nNo lines starting with 'X-DSPAM-Confidence:' were found in the file.")

if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    print("NOTE: You will need a text file (e.g., 'mbox-short.txt') to run this.")
    print("The file should contain lines like 'X-DSPAM-Confidence: 0.8475'.")
    print("----------------------------------------------------------------------")
    analyze_spam_confidence()