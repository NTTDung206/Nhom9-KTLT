filename = input('Enter the file name: ')

if filename == 'na na boo boo':
    print("NA NA BOO BOO TO YOU- You have been punk'd!")
    exit()
else:
    try:
        file = open(filename, 'r')

        count = 0

        for line in file:
            if line.startswith('Subject:'):       
              count = count + 1
        
        print('There are', count, 'subject lines in the', filename)

    except:
        print('File cannot be opened:', filename)