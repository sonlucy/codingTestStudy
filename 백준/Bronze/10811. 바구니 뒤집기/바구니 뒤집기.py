N, M=map(int, input().split())

# arr = [i+1 for i in range(N)]
arr=[*range(1,N+1)]
# res=[]

for _ in range(M):
    a,b = map(int, input().split())

    #(a-1)인덱스부터 b인덱스 전까지 역순. 
    #역순 하는 법 -> arr[::-1]  /  reverse()
  
    # for j in range(a-1,b):
    #     res.append(arr[j])
    # res.reverse()
    # k=0
    # for j in range(a-1,b):
    #     arr[j]=res[k]
    #     k+=1

    arr[a-1:b] = arr[a-1:b][::-1]

print(*arr)
