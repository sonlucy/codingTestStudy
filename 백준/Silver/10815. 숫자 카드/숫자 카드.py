import sys

n = int(sys.stdin.readline())
nList = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

for num in mList:
    if num in nList:
        print(1, end=' ')
    else:
        print(0, end=' ')
