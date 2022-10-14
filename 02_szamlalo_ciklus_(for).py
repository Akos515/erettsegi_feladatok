# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end=",")
print()
lista = [1,2,3,4,5,6,7,8,9,10,11]
for i in lista:
    print(i, end=" ")

# print()
# listaa=["szeretek programozni"]
# for i in listaa:
#     print(f"{i} \n"*4)

print()
for i in [1,2,3,4]:
    print("szeretek progamozni")

for elem in range(0,11,1):
    print(elem)

for elem in range(10):
    print(elem, end=" ")
print()
for elem in range(2):
    print("szeretek programozni")

print(*range(11))

#a végén kiirja hogy vége
for elem in range(11):
    print(elem, end=" ")
else:
    print("vége!")

#szöveg kezelés
for elem in "szöveg":
    print(elem, end="")

print()
gyümölcslista = ["alma", "körte", "banán", "kiwi", "narancs"]
for elem in gyümölcslista:
    print(elem, end=" ")

print(f"A gyümölcsök listában {len(gyümölcslista)} db elem van")

tulajdonsagoklista = ["érett", "nagy", "édes"]
gyümölcslista2 = ["alma", "körte", "banán", "kiwi", "narancs"]

for i in tulajdonsagoklista:
    for j in gyümölcslista2:
        print(i, j)