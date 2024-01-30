arr1=list(map(int, input().split()))
arr2=[1,1,2,2,2,8] # 킹, 퀸, 룩, 비숍, 나이트, 폰 -> 1, 1, 2, 2, 2, 8

# 첫번째 방법 #
result = [str(arr2[i]-arr1[i]) for i in range(6)]
print(" ".join(result))

# 두번째 방법 #
#res=[0]*len(arr1)
#for i in range(6):
    #res[i]=arr2[i]-arr1[i]
    #print(res[i],end=' ')

# 세번째 방법 #
#for i in range(6):
#  print(arr2[i] - arr1[i], end=' ')
