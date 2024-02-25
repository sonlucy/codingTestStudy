N, M=map(int, input().split())
arr=list(map(int, input().split()))
result=0

for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if arr[i]+arr[j]+arr[k]>M:
        continue
      else:
        result=max(result, arr[i]+arr[j]+arr[k])
print(result)

'''
from itertools import combinations

card_num, target_num=map(int, input().split())
card_list=list(map(int, input().split()))
biggest_sum=0

### 두번째 방법 - itertools 라이브러리의 combinations 함수 사용하기
for cards in combinations(card_list, 3):
  temp_sum=sum(cards)
  if biggest_sum<temp_sum <=target_num:
    biggest_sum=temp_sum

print(biggest_sum)
'''