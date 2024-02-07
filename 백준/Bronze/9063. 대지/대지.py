### 첫번째 방법
'''
N=int(input())
x_min=10000; y_min=10000
x_max=-10000; y_max=-10000

for _ in range(N):
  x,y=map(int, input().split())
  if (x<x_min):
    x_min=x
  if (x>x_max):
    x_max=x
  if (y<y_min):
    y_min=y
  if (y>y_max):
    y_max=y

print((x_max-x_min)*(y_max-y_min))
'''

### 두번째 방법
'''
import sys

input = sys.stdin.readline
x_lst = []
y_lst = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))
'''


### 세번째 방법
'''
n = int(input())
min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')

for _ in range(n):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))
'''

### 네번째 방법
n= int(input())
A=[];B=[]
for i in range(n):
  x,y=map(int,input().split())
  A+=[x];
  B+=[y]
print( (max(A)-min(A))*(max(B)-min(B)) )