even=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
length=len(even)
print(length)
del(even[5])
print(even)
length=len(even)
print(length)
var1=6
var2=7
var3=21
if var1 in even:
    print("6 is in the list")
if var2 in even:
    print("7 is in the list")
if var3 not in even:
    print("21 is not in the list")

