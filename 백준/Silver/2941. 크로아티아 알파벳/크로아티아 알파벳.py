alphaList=['c=','c-','dz=','d-','lj','nj','s=','z=']

inputStr=input()

for i in alphaList:
    inputStr=inputStr.replace(i, ' ') # 한 글자로 바꾸기

print(len(inputStr))