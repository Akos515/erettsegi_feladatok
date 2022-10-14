sztring = "Járványhelyzet"
print(sztring)
print(sztring.upper())
print(sztring.lower())
print(sztring.swapcase())
print(sztring[1]) #adott karakter
print(len(sztring))
print(sztring[-1])
for elem in sztring:
    print(elem, end=" ")

print("@"*50)
i = 0
while i < len(sztring):
    print(sztring[i])
    i+=1

print(sztring[0:5])

#karakterek vizsgálata in és a not operátorok:
#in operátor
print("a" in sztring)
if "á" in sztring:
    print("szerepel")
else:
    print("nem szerepel")

#not operator
print("a" not in sztring)