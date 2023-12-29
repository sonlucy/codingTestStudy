a=int(input())
b=input()

for i in list(b)[::-1]:
  print(a*int(i))
print(a*int(b))