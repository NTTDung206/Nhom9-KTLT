# Exercise 3: 

alphabet = 'abcdefghijklmnopqrstuvxwyz'

filename = input("Enter a file name: ")
fhand = open(filename, 'r')
text = fhand.read()

freq_dict = {}
for ch in text.lower():
    if ch in alphabet:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

lst = []
for key, value in freq_dict.items():
    lst.append((value,key))

lst.sort(reverse=True)
for freq, letter in lst:
    print(letter, freq)
