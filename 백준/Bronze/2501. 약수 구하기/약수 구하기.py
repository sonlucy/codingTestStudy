import sys

n, k= map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n+1) if (n%i==0)] # 약수를 차례대호 저장(오름차순)

if len(arr)<k: #k번째 약수 존재하지 않으면(약수의 개수가 k개보다 작음) 0출력
  print('0')
else:
  print(arr[k-1]) # k번째로 작은 수 출력