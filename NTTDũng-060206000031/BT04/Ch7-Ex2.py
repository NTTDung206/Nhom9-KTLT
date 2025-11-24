filename = input('Enter the file name: ')
file = open(filename, 'r')

count = 0
total = 0

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        index = line.find(' ')
        num = float(line[(index+1):])
        count = count + 1
        total = total + num

print('Average spam confidence: ', total/count)