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
#