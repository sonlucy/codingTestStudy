a,b,c= map(int, input().strip().split(' '))

if (a!=b and a!=c and b!=c):
    print(100*max(a,b,c))
elif (a==b and b==c):
    print(10000+a*1000)
else:
    if (a==b) or (a==c):
        print(1000+a*100)
    else:
        print(1000+b*100)