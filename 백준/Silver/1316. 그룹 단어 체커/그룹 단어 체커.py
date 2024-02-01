n=int(input()) #입력받을 단어 개수
#arr=[]
cnt=0 #그룹단어 개수 저장

for _ in range(n):
    word=input()
    #arr.append(word[0]) #첫번째 알파벳 arr에 추가
    arr = [word[0]]
    for j in range(len(word)-1):
        if word[j]!=word[j+1]: #현재문자와 다음 문자가 다르면
            arr.append(word[j+1]) # arr에 추가

  
    # if list(dict.fromkeys(word))==arr:  #중복 없앤 문자열과 arr가 같으면 그룹단어
    if len(set(word))==len(arr):  # 중복 없앤 문자열의 길이와 arr 길이 같으면 그룹단어
        cnt+=1 # 그룹단어이므로 cnt 증가
    #arr=[] #arr 초기화

print(cnt)
