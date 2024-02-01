N, B= input().split()
B=int(B) # 사용할 진법. 2 <= B <= 36

'''
arrDict=['A':10, 'B':11,'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, ]
'''
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Z:35
'''
2진법 -> 10진법:
제곱승씩 곱해서.

110 -> 2의 1승*1 + 2의 2승*1= 2+4= 6
자리수*1의 자리수는 B의0승
'''


result=0
j=len(N)-1 # 입력받은 수 N의 길이 -1 => N의 가장 왼쪽 숫자의 자리 수
for i in range(0,len(N)):
  result+=(B**j)* num.index(N[i]) # B의 j승 * N에서 해당 자리수의 수를 10진수로 변환한 것
  j-=1

print(result)