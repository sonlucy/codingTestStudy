N,M=map(int, input().split())
result=[]
arr=[]
for i in range(N):
  arr.append(input())

#8X8로 잘라서 나오는 체스판 개수 만큼 반복
for i in range(N-7):
  for j in range(M-7):
    whiteStartCase=0
    blackStartCase=0
    #여기서부터 정해진 8x8 체스판에 대해 바꿔야하는 정사각형 개수를 셀거얌
    #맨 위 왼쪽이 흰색인 경우와 검정색인 경우 두 경우에 대해 바꿔야하는 개수 셀거얌
    for a in range(i,8+i):
      for b in range(j,8+j):
        #i+j가 짝수/홀수 -> 검정/흰 or 흰/검정
        if (a+b)%2==0:
          if arr[a][b]=='W': 
            blackStartCase+=1
          else:
            whiteStartCase+=1
        else:
          if arr[a][b]=='W':
            whiteStartCase+=1
          else:
            blackStartCase+=1
        
    result.append(whiteStartCase)
    result.append(blackStartCase)

print(min(result))
        