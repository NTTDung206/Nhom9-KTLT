hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
x = hours
y = rate

if x > 40:
    pay = (x - 40) * 1.5 * y + 40 * y
else:
    pay = x * y
print("pay:", pay)