n=int(input())
arr=[]

for _ in range(n):
  x,y=map(int, input().split())
  arr.append((x,y))

arr.sort()
for i in range(n):
  print(arr[i][0], arr[i][1]) #i번째 (x,y) 출력
  