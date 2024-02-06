
import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
'''
arr=[]
for i in range(N, M+1):
  if num < 2:
      arr.append(i)
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          break #소수가 아님
  arr.append(i)
if len(arr)==0: #소수가 없을 경우
  print('-1')
else:
  print(sum(arr)) # 합 출력
  print(min(arr)) # 최솟값 출력
  '''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [i for i in range(N, M+1) if is_prime(i)]

if not primes:
    print('-1')
else:
    print(sum(primes))
    print(min(primes))