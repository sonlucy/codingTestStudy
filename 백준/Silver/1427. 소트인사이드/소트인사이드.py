'''
n=int(input())
digitList=list(map(int, str(n)))
digitList.sort(reverse=True)
for i in digitList:
  print(i, end='')
'''

n = int(input())
digit_list = sorted(str(n), reverse=True)
print(''.join(digit_list))
