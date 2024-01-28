str=list(input())

#(8+2)+ (1+2)

#1 -> 2초
#65-67: 2 -> 2+1초
#68-70: 3 ->
#71
sumOf = 0

for i in str:
  if 65<=ord(i)<=67: #ABC
    sumOf+=1
  elif 68<=ord(i)<=70: #DEF
    sumOf+=2
  elif 71<=ord(i)<=73: #GHI
    sumOf+=3
  elif 74<=ord(i)<=76: #JKL
    sumOf+=4
  elif 77<=ord(i)<=79: #MNO
    sumOf+=5
  elif 80<=ord(i)<=83: #PQRS
    sumOf+=6
  elif 84<=ord(i)<=86: #TUV
    sumOf+=7
  elif 87<=ord(i)<=90: #WXYZ
    sumOf+=8
  else: #operator
    sumOf+=9
    '''
for i in range(len(str)):
  if 65<=ord(str[i])<=67: #ABC
    sum+=1
  elif 68<=ord(str[i])<=70: #DEF
    sum+=2
  elif 71<=ord(str[i])<=73: #GHI
    sum+=3
  elif 74<=ord(str[i])<=76: #JKL
    sum+=4
  elif 77<=ord(str[i])<=79: #MNO
    sum+=5
  elif 80<=ord(str[i])<=83: #PQRS
    sum+=6
  elif 84<=ord(str[i])<=86: #TUV
    sum+=7
  elif 87<=ord(str[i])<=90: #WXYZ
    sum+=8
  else: #operator
    sum+=9
    '''
sumOf+= len(str)*2
print(sumOf)