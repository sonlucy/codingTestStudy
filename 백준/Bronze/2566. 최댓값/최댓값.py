arr=[0]*9
for i in range(9):
    arr[i]=list(map(int, input().split()))

for i in range(9):
    for j in range(9):
        if arr[i][j]==max(map(max, arr)):
            a,b=i+1,j+1

print(max(map(max, arr)), a,b)