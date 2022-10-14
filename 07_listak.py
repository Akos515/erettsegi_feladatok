ureslista = []
szamoksliasta = [14,25,36,48,52,66,72,83,97,105]
szoveglista = ["alma", "virág", "kutya", "ember"]
listalistaban = [4, 5, 8, 3, [8, 6 ,7 ,2]]
vegyeslista = ["szöveg", 4, 3, ["szövegek", 5, 7, 4.5]]

print(ureslista, szoveglista, szamoksliasta, listalistaban, vegyeslista)

#adott elemének elérése
print(szoveglista[2])

#egesz lista
for i in szamoksliasta:
    print(i, end=" ")

print(*vegyeslista)

#lista műveletek
osszead = szamoksliasta + szamoksliasta
print(osszead, end=" ")

#szorzat
szorzas = szamoksliasta * 2
print(szorzas)
for szorzat in szamoksliasta:
    print(szorzat*2, end=" ")
print()

#szeletelés
print(szamoksliasta[5:9])

szoveglista[2] = "FALIÓRA"
print(szoveglista)

szoveglista[1:1] = "kutya"
print(szoveglista)

print(szamoksliasta)
del szamoksliasta[2]
print(szamoksliasta)

szamoksliasta.append(3)
print(szamoksliasta)

for i in range(len(szamoksliasta)):
    print(f"{i} => {szamoksliasta[i]*2}")
print("-"*50)
#szebben

for index, elem in enumerate(szamoksliasta):
    print(f"{index} => {elem*2}")