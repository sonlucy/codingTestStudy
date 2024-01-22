n = int(input())
# list(range(1,n+1))
cnt=1  ## 숫자 n만 뽑는 경우의 수를 미리 넣어둔다
Sum=1
start_idx=1
end_idx=1

while end_idx != n:
  if Sum < n:
    end_idx+=1
    Sum += end_idx
  elif Sum > n: # 기준으로 하는 값보다 큰 값이 나오면
    Sum -= start_idx # 원래 더했던 start_idx를 빼줌
    # start_idx를 +1 전진
    start_idx+=1
  elif Sum == n:
    cnt += 1
    end_idx += 1
    Sum += end_idx
    
print(cnt)

