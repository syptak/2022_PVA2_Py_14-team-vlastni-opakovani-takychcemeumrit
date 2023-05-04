#1
#   a)
jmeno_prijmeni = input ("Zadejte jméno a příjmení: ")

#   b)
print ("Vítejte, " + jmeno_prijmeni + "!")

#2
cislo_1 = int(input ("Vložte číslo: "))
cislo_2 = int(input ("Vložte další číslo: "))

if cislo_1 > cislo_2:
    print("První číslo je větší než druhé číslo.")
elif cislo_1 < cislo_2:
    print("Druhé číslo je větší než první číslo.")
else:
    print("Zadaná čísla jsou stejná.")

soucin = cislo_1 * cislo_2

print("Součin zadaných čísel je:", soucin)