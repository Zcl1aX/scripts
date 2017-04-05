with open('FileName', 'rb') as f:
    data = f.read()
f.close()

mn = {68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90}  # +3
mn1 = {65,66,67}
new_d = b''

for a in data:
    if a in mn:
        new_d += bytes([a - 3])
    elif a in mn1:
        new_d += bytes([a + 23])
    else:new_d += bytes([a])


print(type(new_d))
f = open('filename', 'wb')
f.write(new_d)
f.close()
