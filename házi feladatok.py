# valaszosszeg = int(input("kérek egy összeget:"))
# befizetettszamla = 0
# osszszamla = 0
#
# for elem in range(10):
#     valaszszamla = int(input("kérem a számlát:"))
#     osszszamla += valaszszamla
#     if valaszosszeg == valaszszamla or osszszamla <= valaszosszeg and valaszosszeg > valaszszamla:
#         befizetettszamla += 1
#     else:
#         print("nincs elég pénzem")
#         osszszamla -= valaszszamla
#         break
# print(f"a befizetett számlák száma: {befizetettszamla}, az összegük {osszszamla}")
#
# # Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna)
# # jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
# # - egyikük sem jön kosarazni,
# # - mind a ketten jönnek kosarazni,
# # - csak az egyikük jön kosarazni.
#
# henrik = (input("Jön Henrik ma kosarazni?: "))
# hanna = (input("Jön Hanna ma kosarazni?: "))
# if henrik == "igen" and hanna == "igen":
#     print("mind a ketten jönnek kosarazni.")
# elif henrik == "igen" and hanna == "nem" or henrik == "nem" and hanna == "igen":
#     print("csak az egyikük jön kosarazni.")
# else:
#     print("egyikük sem jön kosarazni.")
# print()
#
# # Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
# # - csak 3-mal osztható,
# # - csak 4-gyel osztható,
# # - 3-mal és 4-gyel is osztható,
# # - sem 3-mal, sem 4-gyel nem osztható!
#
# valasz = int(input("Kérek egy számot: "))
# if valasz % 3 == 0 and valasz % 4 == 0:
#     print("3-mal és 4-gyel is osztható")
# elif valasz % 3 == 0 and not valasz % 4 == 0:
#     print("csak 3-mal osztható")
# elif valasz % 4 == 0 and not valasz % 3 == 0:
#     print("csak 4-gyel osztható")
# else:
#     print("sem 3-mal, sem 4-gyel nem osztható!")

#lista = [0, 1]
# a = lista[0]
# b = lista[1]
length = int(input("Kérek egy hosszúságot: "))
# for i in range(length):
#     c = a+b
#     lista.append(c)
#     a = b
#     b = c
# print(lista)
list = [0, 1]
for g in range(length):
    c = list[0+g]+list[1+g]
    list.append(c)
print(list)


hely = 0
szo = "befogadóképességű"
valasz = input("Kérek egy betűt: ")
if valasz in szo:
    print("Találat!")
    for i in szo:
        if valasz in i:
            print(f"A betű a {hely + 1} helyen található")
        hely += 1
else:
    print("Nem található!")

