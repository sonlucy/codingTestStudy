n=int(input())
#arr=list(map(int, input().split('')))
a=int(input())
arr=[]
k=1
for i in range(n):
    arr.append(a//k%10)
    k*=10
arr.reverse()    
sum=0
for i in range(n):
    sum+=arr[i]
print(sum)