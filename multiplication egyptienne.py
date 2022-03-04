a = int(input())
b = int(input())
c = 0
while a != 0:
    if a%2 == 1:
        c += b
    a //= 2
    b += b
print(c)