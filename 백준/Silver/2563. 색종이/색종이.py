n = int(input())

# 도화지의 크기는 100 X 100
#paper = [[0]*100 for i in range(100)] 
paper=[[0 for j in range(100)] for i in range(100)]

for _ in range(n):
    x, y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

result = 0
for i in paper:
    result += sum(i)
print(result)