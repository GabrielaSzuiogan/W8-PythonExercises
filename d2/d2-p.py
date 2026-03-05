#1
num = int(input("Introduceti un numar: "))
if num == 0:
    print("Numarul este zero")
elif num > 0:
    print("Numarul este pozitiv")
else:
    print("Numarul este negativ")


#2 
if num % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")


#3
lit = input("Introduceti o litera: ")
if lit in 'aeiouAEIOU':
    print("Litera este o vocala")
else:
    print("Litera este o consoana")


#4
age = int(input("Introduceti varsta: "))
if age < 18 or age > 65:
    print("Aveti reducere!")
else:
    print("Nu aveti reducere!")

#5
year = int(input("Introduceti un an: "))
if year % 4 == 0 and year < 100:
    print("Anul este bisect")
elif (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print("Anul este bisect")
else: 
    print("Anul nu este bisect")