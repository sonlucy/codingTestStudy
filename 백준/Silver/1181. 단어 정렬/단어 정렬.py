import sys

n=int(input())
arr=[]
for _ in range(n):
  arr.append(sys.stdin.readline().strip())

arr=list(set(arr)) #중복제거 후, 리스트 자료형으로 변환
arr.sort() #사전 순으로 정렬
arr.sort(key=len) #길이가 짧은 것부터 정렬
for i in arr:
  print(i) 
  