mlist = []
number = int(input("input n:"))
for i in range(number):
    x = int(input("input x:"))
    mlist.append(x)
print(mlist)

result = []
for num in mlist: # по значениям
    if num%2 == 0:
        result.append(num)
print(result)

