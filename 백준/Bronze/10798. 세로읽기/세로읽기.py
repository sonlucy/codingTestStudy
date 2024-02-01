arr=[input() for _ in range(5)] # 5줄 동안 input 받기
max_length = max(map(len, arr)) # arr에 있는 문자열 중에 길이가 가장 긴 문자열의 길이를 구함
for j in range(max_length): # 
    for i in range(5): # 5줄에 대해
            if j < len(arr[i]): # 문자가 있는 부분에서만 문자를 출력하기 위해.
                    print(arr[i][j], end='')