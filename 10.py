a = float(input())
c = 0
while a != 0:
    b = a
    a = float(input())
    if a != 0 and a < b:
        c+=1
print(c)