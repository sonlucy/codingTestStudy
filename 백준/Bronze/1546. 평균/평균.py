n=int(input())
arr=list(map(int, input().split()))

M=max(arr)
######## 방법2 #########
# for i in range(n):
#     arr[i]= arr[i]/M*100
# print(sum(arr)/num)
print(sum(arr)/M*100/n)