import sys
input=sys.stdin.readline

s=input().strip()
'''
arr=[]

for i in range(len(s)):
  for j in range(i, len(s)):
    arr.append(s[i:j+1])
    
arr=set(arr)
'''
arr=set()


for i in range(len(s)):
  for j in range(i + 1, len(s) + 1):
      arr.add(s[i:j])

print(len(arr))