a = input().split()
x = 0
for i in a:
    i = int(i)
    if i > 0 and i < 1000:
        x += 1
print(x)