#1
jmeno = input ("Zadejte jmeno: ")
prijmeni = input ("Zadejte příjmení: ")
input ("Kolik máš let: ")
input ("Kde bydlíš: ")

#2
milimetry = float(input("Zadejte hodnotu v milimetrech: "))
centimetry = milimetry * 0.1
print(f"{milimetry} mm je {centimetry} cm")

#3
a = 10
b = 40


if a < b:
    print("a je mensi nez b")
elif a > b:
    print("a je vetsi nez b")
else:
    print("a a b jsou stejne")
#4
celejmeno = jmeno + "" +prijmeni
print(celejmeno)

#4
c = input("Zadejte hodnotu: ")
d = input("Zadejte hodnotu: ")
f = abs(c, d)
soucin = c * d
print(soucin)