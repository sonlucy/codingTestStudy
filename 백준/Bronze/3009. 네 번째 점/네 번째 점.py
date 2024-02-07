'''
### 첫번째 방법
x1,y1= map(int, input().split())
x2,y2= map(int, input().split())
x3,y3= map(int, input().split())

if x1==x2:
  x4=x3
elif x1==x3:
  x4=x2
else:
  x4=x1

if y1==y2:
  y4=y3
elif y1==y3:
  y4=y2
else:
  y4=y1

print(x4,y4)
'''


'''
### 두번째 방법
# 세 점의 좌표 입력받기
points = [tuple(map(int, input().split())) for _ in range(3)]

# x좌표와 y좌표를 따로 넣기
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# 유일한 x, y 좌표 찾기
x4 = next(x for x in x_coords if x_coords.count(x) == 1)
y4 = next(y for y in y_coords if y_coords.count(y) == 1)

print(x4, y4)

'''

### 세번째 방법
m,n=0,0 # 좌표값들을 xor 연산을 통해 쌓아가기위해 0으로 초기화
for i in range(3):
  x, y=map(int,input().split())
  # XOR(^) 연산으로 유일한 값을 찾는다.
  m ^= x
  n ^= y
print(m,n)