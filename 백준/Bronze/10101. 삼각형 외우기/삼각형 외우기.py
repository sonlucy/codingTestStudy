### 첫번째 방법
'''
a=int(input())
b=int(input())
c=int(input())

if a+b+c==180:
  if a==b==60: #세 각의 크기가 모두 60이면, Equilateral
    print('Equilateral')
  elif a!=b and b!=c and a!=c: # 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
    print('Scalene')
  else: # 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
    print('Isosceles')
else: # 세 각의 합이 180이 아닌 경우에는 Error
  print('Error')
  '''

### 두번째 방법
angles = [int(input()) for _ in range(3)]

if sum(angles) == 180:
    if len(set(angles)) == 1:
        print('Equilateral')  # 모든 각이 같으면 Equilateral
    elif len(set(angles)) == 2:
        print('Isosceles')    # 두 개의 각이 같으면 Isosceles
    else:
        print('Scalene')      # 모든 각이 다르면 Scalene
else:
    print('Error')             # 삼각형의 각의 합이 180이 아니면 Error