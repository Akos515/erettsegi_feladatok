#képernyőre kiiratás
print("Első programom!")        #futtatáshoz shift+ctrl+f10
print('Első programom!')        #vagy így
#print('Első programom! "idézet" ')
#print("Első programom! "idézet" ")     #hibás

#több sorban való kiiratás
print("""
valami
valami2
""")
#érték típusok
15          #int
"szöveg"    #str (string)
3.15        #float (lebegő pontos)

#változó
a = 0
print(a)
a = 15      #int típus szám
print(a)
szoveg = ""     #üres string típusú változó
szoveg = "Ez egy szöveg!"
print(type(szoveg))
print(szoveg)

#változó értéknövelés
b = 0
print(b)
b = b+1
print(b)

b += 10
print(b)

b *= 5
print(b)

#b =* 5     (nem jó)

#váltotó típusának megváltoztatása
nap = "süt a nap"
print(type(nap))
print(nap)
nap = 2022
print(type(nap))
print(nap)

#beépített függvény
nev = "Németh Ákos"
hossz = len(nev)
print(hossz)

#egyben
print(len(nev))

#változó művelet összeadások
c = 8
d = 5
e = c+d
print(e)

#kiiratás szöveggel:
print("Az e változóm értéke: e")
print("Az e változóm értéke:", e)
print("Az e változóm értéke: "+str(e))
print(f"Az e változóm értéke: {e}")

#típuskonverzió
#ezek a sorok nem egyenlőek a változók típusaival
int(15)
str(15)
float(15)

#műveletek

#összeadás +
#kivonás -
#szorzás *
#hatványozás **
#osztás maradéka %
#osztás / vagy //

f = e/3         #maradékos osztás
print(f)

f = e//3        #egészre kerekített osztás
print(f)

g = e**2        #hatványozás
print(g)

h = e%d         #az osztás maradéka
print(h)

#zárójelek
i = 5
i = 3*i+1
print(i)
i = 5
i = 3*(i+1)
print(i)

#szöveg összefűzése + jel segítségével
vnev = "Németh"
knev = "Ákos"
print(vnev+" "+knev) #a " "-ek között space van, ezt szúrja be

#de ez nem összefűzés
print(f"{vnev} {knev}")


nev = vnev+knev
print(nev)

nev = f"{vnev} {knev}"      #változóban f string
print(nev)

#adatok bekérése egy embertől
#input("Kérek egy keresztnevet: ")
#print(input("Kérek egy keresztnevet: "))

# valasz = input("Kérek egy nevet: ")
# print(valasz)

#valaszvnev = input("Kérek egy vezetéknevet: ")
#valaszknev = input("Kérek egy keresztnevet: ")

#print(f"A kért adat: {valaszvnev} {valaszknev}")

#kérj be két számot és irasd ki az összegüket

# szám1 = int(input("első szám:"))
# szám2 = int(input("második szám:"))
# print(f"A két szám összege: {szám1+szám2}")

#lista létrehozása
lista = []          #üres lista
print(type(lista))
print(lista)

lista = [1, 5, 7, 9]
print(lista)

#lista adott elemének elérése
lista = ["alma", "körte", "banán"]
print(lista[0])     #első elem
print(lista[-1])    #utolsó elem