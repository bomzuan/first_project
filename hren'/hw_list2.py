mlist = []
number = int(input("enter a number:"))
for i in range(number):
    x = int(input("input x:"))
    mlist.append(x)
print(mlist)

for i in range(number): #по индексам
    if i%2 == 0:
        print(mlist[i])

