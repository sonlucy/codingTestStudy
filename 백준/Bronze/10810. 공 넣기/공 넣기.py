N, M=map(int, input().split())

list=[0]*N

for _ in range(M):
    a,b,c=map(int, input().split())

    list[(a-1):b] = [c]*(b-a+1) #길이가 (b-a+1)이고 각 요소가 c인 리스트가 할당됨
    # for j in range(a-1, b): 
    #     list[j]=c

print(*list)
# for i in list:
#   print(i,end=' ')