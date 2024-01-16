#아스키코드값이 97부터 122까지니까 (아스키-97)로 하면 0부터 된다
#a:0 b:1 c:2 ,.. . falut:-1로
#ord: 문자 -> 아스키코드값
#chr: 아스키코드값 -> 문자

str=input() 
output=[-1]*26

for i in range(len(str)):
  if output[ord(str[i])-97]!= -1: #o가 두번 나오는데, 그 중 처음 나오는 o의 인덱스를 출력하니까 이미 -1이 아닌 값이면 변경 없이 고고.
    continue
  else: 
    output[ord(str[i])-97] = i #i는 str을 보는 인덱스!

for i in range(26):
  print(output[i],end=' ')
