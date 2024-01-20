x=int(input())
for _ in range(x):
  a, b= map(str, input().split())
  for c in b:
    print(c*int(a),end='')
  print()