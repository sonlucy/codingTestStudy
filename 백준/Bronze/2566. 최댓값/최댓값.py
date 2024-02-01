table = [list(map(int, input().split())) for _ in range(9)]

# 첫번째 방법 #
'''
for i in range(9):
  for j in range(9):
    if table[i][j]==max(map(max, table)): # 현재 위치가 테이블에서 가장 큰 값이면
      row_idx, col_idx = i+1 ,j+1 #현재 위치를 저장
print(max(map(max, table)), row_idx, col_idx)
'''
# 두번째 방법 #
max_value = max(map(max, table))
for row, col_list in enumerate(table): # 각 행을 순회
  if max_value in col_list: # 맥스값이 있으면
    print(max_value, row + 1, col_list.index(max_value) + 1)
