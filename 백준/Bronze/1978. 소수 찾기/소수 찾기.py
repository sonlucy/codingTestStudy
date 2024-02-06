import sys
n=int(sys.stdin.readline())
'''
arr=list(map(int, sys.stdin.readline().split()))
cnt=0
for i in arr:
  if i==1:
    continue
  elif i==2:
    cnt+=1
  else:
    for j in range(2,i):
      if i%j==0: #딱 나눠떨어지는 수가 하나라도 있으면 소수가 아님
        break
      if j==i-1:
        cnt+=1 

print(cnt)
'''
# 두번째 방법
def is_prime(num):
  if num < 2:
      return False #소수가 아님
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False #소수가 아님
  return True # 소수임

arr = map(int, sys.stdin.readline().split())

cnt = sum(1 for i in arr if is_prime(i))
print(cnt)