import sys

arr=[25, 10, 5, 1]  #쿼터, 다임, 니켈, 페니
n=int(input())

for _ in range(n):
  c=int(sys.stdin.readline())

  for coin in arr:
    print(c//coin, end=' ')
    c %= coin
  print()