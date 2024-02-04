
N=int(input())
cnt=1

while(N>cnt):
  N-=cnt
  cnt+=1

if cnt%2==0:
  '''
  앞에거는 오름차순,
  뒤에거는 내림차순
  '''
  print(f'{N}/{cnt-N+1}')
else:
  print(f'{cnt-N+1}/{N}')