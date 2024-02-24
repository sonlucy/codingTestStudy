### 첫번째 방법
'''
N= int(input())
N-=2
i=1
result=0
while (N>0):
  result+=N*i
  N-=1
  i+=1
print(result)
print('3')

'''

### 두번째 방법
N= int(input())
print(N*(N-1)*(N-2)//6)
print('3')
