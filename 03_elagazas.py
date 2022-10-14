#feltételes végrehajtás

#két változó a kisebb mint b
a = 225
b = 36

if a < b:
    #igaz ág
    print(f"az {a} szám kisebb mint a {b} szám")
else:
    #hamis ág
    print(f"az {a} szám nagyobb mint a {b} szám")

# i = int(input("Adj meg egy számot: "))
# if i % 2 == 0:
#     print("páros")
# else:
#     print("páratlan")

# i = int(input("Adj meg egy számot: "))
# if i > 0:
#     print("pozitív")
# else:
#     print("negatív")

# i = int(input("Adj meg egy számot: "))
# if i > 0:
#     print("a szám pozitív")
# else:
#     if i == 0:
#         print("a szám 0")
#     else :
#         print("a szám negatív")

# i = int(input("Adj megy egy számot: "))
# if i < 10 and i > 0:
#     print("a szám 0 és 10 közé esik")
# else:
#     print("a szám vagy nagyobb 10nél vagy kisebb mint 1")
print("milyen színű a fű?")
print('"a" a fű kék,\n"b" a fű zöld,\n"c" a fű piros')
valasz = input('Melyik a helyes válasz, "a", "b" vagy "c"?')
if valasz == "a":
    print("a fű kék")
elif valasz == "b":
    print("a fű zöld")
elif valasz == "c":
    print("a fű piros")
else:
    print("rossz válasz")