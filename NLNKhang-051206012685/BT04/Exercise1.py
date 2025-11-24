filename = input("Enter a file name: ")

try:
    file = open(filename)
    for line in file:
        line = line.rstrip()  # Xóa ký tự xuống dòng ở cuối
        print(line.upper())   # In dòng với chữ in hoa
except:
    print("File cannot be opened:", filename)