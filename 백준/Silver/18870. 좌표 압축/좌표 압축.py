import sys
n=int(input())
arr=list(map(int, sys.stdin.readline().strip().split()))
arr_set=sorted(set(arr))
#인덱스번호대로 출력. a[0]=2라면, 2는 0을 출력
#근데 이렇게 하면 인덱스번호가 겹칠 수 있으니까 반대로
#a[2]=0 형태로 할거임.
#중복되는 값을 제거해주었으니 위의 형태는 겹칠 일 없음.
# 따라서 dict의 key value를 이용.
'''
dic={}
for i in range(len(arr2)):
  dic[arr_set[i]]=i

for i in range(len(arr)):
  print(dic[arr[i]], end=' ')
'''
# 딕셔너리를 사용하여 각 요소의 값에 대한 인덱스 매핑
index_map = {value: idx for idx, value in enumerate(arr_set)}

# 각 요소의 값에 대해 딕셔너리에서 인덱스를 찾아 출력
result = [index_map[value] for value in arr]
print(' '.join(map(str, result)))  # 결과 출력
  