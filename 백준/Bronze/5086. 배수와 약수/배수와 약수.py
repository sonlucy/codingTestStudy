import sys

while(1):
  a, b= map(int, sys.stdin.readline().split())
  #a, b=map(int, input().split())

  if a==b==0:
    break

  if (b%a==0): # 첫번째 숫자가 두번째 숫자의 약수
    print('factor')
  elif (a%b==0): # 첫번째 숫자가 두번째 숫자의 배수
    print('multiple')
  else: # 첫번째 숫자가 두번째 숫자의 약수와 배수 모두 아님
    print('neither')
