import sys

n=int(sys.stdin.readline())
arr=[]

for _ in range(n):
  a,b=sys.stdin.readline().strip().split()
  if b=='enter':
    arr.append(a)
  elif b=='leave':
    arr.remove(a)

arr.sort(reverse=True)
for i in arr:
  print(i)
