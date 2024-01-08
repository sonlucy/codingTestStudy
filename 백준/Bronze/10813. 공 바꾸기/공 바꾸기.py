N, M=map(int, input().split())

# arr=[0]*1000
# for i in range(N):
#   arr[i]=i+1 
arr =[i+1 for i in range(N)]

for i in range(M):
  a, b=map(int, input().split())
  arr[a-1], arr[b-1]=arr[b-1], arr[a-1]

# for i in range(N):
#   print(arr[i],end=' ')
print(*arr)
