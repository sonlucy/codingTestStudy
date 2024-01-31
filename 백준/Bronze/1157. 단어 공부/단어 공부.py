words=list(input().upper()) # 대문자 변환
word=list(set(words)) #set()은 중복을 제거한 리스트를 반환

cnt=[]

for i in word:
    cnt.append(words.count(i)) #입력리스트에 i번째 요소가 몇개들어있는지 cnt에 추가

if cnt.count(max(cnt))>1: #최댓값이 여러개면
    print('?')
else:
    print(word[cnt.index(max(cnt))])
