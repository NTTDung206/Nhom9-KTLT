# Exercise 1
Hours = float(input('Enter Hours: '))
Rate = float(input('Enter Rate: '))
if Hours > 40:
    Pay = 40 * Rate + (Hours - 40) * Rate * 1.5
else:
    Pay = Hours * Rate
print("Pay:" , Pay)