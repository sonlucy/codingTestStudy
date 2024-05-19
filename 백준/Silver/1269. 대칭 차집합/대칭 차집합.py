import sys
input=sys.stdin.readline
n,m=map(int,input().strip().split())

arrN=set(map(int, input().split()))
arrM=set(map(int, input().split()))

#print(len(arrN-arrM)+len(arrM-arrN))
print(len(arrN ^ arrM))