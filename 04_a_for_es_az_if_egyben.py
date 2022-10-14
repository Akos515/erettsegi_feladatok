list = [5,47,8,54,6,2,15,4,1,25,10,65,17,321]
#irassuk ki a húsznál kisebb számokat
for i in list:
    if i > 20:
        print(i, end=" ")
print()
for i in list:
    if i == 10:
        break
    print(i, end=" ")
