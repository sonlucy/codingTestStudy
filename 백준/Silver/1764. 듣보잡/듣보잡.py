import sys
input=sys.stdin.readline

arr1=set()
arr2=set()

n,m=map(int, input().strip().split())

for _ in range(n):
  arr1.add(input().strip())

for _ in range(m):
  arr2.add(input().strip())

#result=arr1&arr2
result = arr1.intersection(arr2) #교집합

result=sorted(result)

print(len(result))
for i in result:
  print(i)