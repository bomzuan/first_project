phrase = "don't panic" # "on tap"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.insert(2, " ")
plist.pop(4)
plist.insert(4, "a")
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)