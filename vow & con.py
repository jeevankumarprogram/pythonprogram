name=input("enter the name")
vow="aAeEiIoOuU"
V,C=0,0
for i in name:
    if i in vow:
        v +=1
    else:
        c +=1
print("the string has()vowels and ()consonats".formate(v,c))
