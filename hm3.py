x = int(input("How many tickets do you need?:"))
y = x % 60
z = (x - y)// 60
a = y % 10
b = (y - a)// 10
if a > 8:
    b += 1
    a = 0
print(a, b, z)
