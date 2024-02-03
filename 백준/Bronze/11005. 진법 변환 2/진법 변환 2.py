N, B= map(int, input().split())

num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Z:35

'''
나머지 (%) 넣는데, N=1일때 마지막으로 나머지 계산해서 넣고 끝.
출력할땐 역순으로 출력
'''

result='' #문자열로 저장할거임

while (N>=1):
  result+=num[N%B]
  N=N//B

print(result[::-1]) #문자열을 역순으로 출력