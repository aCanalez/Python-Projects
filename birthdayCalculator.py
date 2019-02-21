from datetime import datetime
from datetime import timedelta
from datetime import date
now = datetime.now()

print(now)
print("When where you born? enter in single line like xxxxxxxx")
birthDate = str(input())

print(birthDate)

birthStringFormatted = datetime.strptime(birthDate, '%m%d%Y')
print("Birth String Formatted " + str(birthStringFormatted))
calculated = date.today() - datetime.date(birthStringFormatted)

print(calculated)

timeVariable = int((input("How many years in the future would you like to know your next birthday?")) * 365) + 5
t = birthStringFormatted + timedelta(days=timeVariable)
s = t.strftime("%A %B %d, %Y")

print("Your next birthday will be " + s)
