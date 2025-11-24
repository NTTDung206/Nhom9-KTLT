str = 'X-DSPAM-Confidence:0.8475'
f = str.find(':')
slic = str[(f+1):]
num = float(slic)
print(num)