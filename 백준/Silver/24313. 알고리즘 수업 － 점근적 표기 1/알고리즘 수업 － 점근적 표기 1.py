a1,a0= map(int, input().split()) 
c=int(input())
n0=int(input())

### 첫번째 방법
'''
n=n0
while(n>=n0): # 
  if a1*n+a0>c*n: #f(n)= a1*n+a0, 조건 만족하지 않는게 있으면(f(n)>cn)) 
    print('0') # 0 출력
    break
  n+=1
  if n>100:
    print('1') # O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
    break
'''

### 두번째 방법
n=n0
if ((a1*n+a0 <= c*n) & (a1<=c)): # a1은 f(n)의 일차항(최고차항), c는 g(n)의 일차항(최고차항)의 계수이기 때문에, a1이 무조건 c보다 작거나 같아야 함
  print(1)
else:
  print(0)

# n이 무한대로 갈수록, 상수항은 무의미해짐