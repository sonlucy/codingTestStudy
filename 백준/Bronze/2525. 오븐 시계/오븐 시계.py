h, m = map(int, input().strip().split(' '))
e= int(input())

m+=e
if (m>=60):
    a= m//60
    m-=60*a
    h+=a
    if (h>=24):
        h-=24
print(h, m)