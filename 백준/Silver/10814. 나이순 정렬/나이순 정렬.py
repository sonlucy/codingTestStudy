import sys

n=int(input())
arr=[]

for _ in range(n):
  age, name=sys.stdin.readline().strip().split()
  age=int(age)
  arr.append((age, name))

arr.sort(key= lambda arr:arr[0]) #age만 가지고 정렬하깅

for i in range(n):
  print(arr[i][0], arr[i][1])