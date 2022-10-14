#valasz = int(input("kérek egy számot: "))
# osszeg = 0
# kezdoszam = 1
# while kezdoszam <= valasz:
#     osszeg += kezdoszam
#     kezdoszam += 1
# print(osszeg)

# osszeg2 = 0
# for i in range(valasz+1):
#     osszeg2 += i
# print(osszeg2)

#hátul tesztelős ciklus
# while True:
#     jelszo = input("Kérem a jelszót: ")
#     jelszoujra = input("Jelszó megerősítése: ")
#     if jelszo == jelszoujra:
#         break
#     print("A két jelszó nem egyezik, próbáld újra!")
# print("Ok! Köszönöm.")

#középen tesztelős ciklus
# osszeg3 = 0
# while True:
#     valasz = input("kérek egy számot! (Az enter leütésével megszakíthatod a folyamatot.)\n a szám: ")
#     if valasz == "":
#         break
#     osszeg3 += int(valasz)
# print(f"A bekért számok összege: {osszeg3}")

while True:
    try:
        valasz = int(input("kérek egy számot: "))
    except ValueError:
        print("nem szám")
    else:
        print(f"ok! A beírt szám: {valasz}")
        break
valaszszoveg = input("Kérek egy szöveget: ")

while valaszszoveg.isdigit() == True:
    valaszszoveg = input("Szöveget adj meg:")