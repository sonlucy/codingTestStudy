
arr=[0]*30
for i in range(30):
    arr[i]=i+1

for i in range(28):
    a=int(input())
    if (1<= a <= 30):
        arr.remove(a)
print(min(arr))
print(max(arr))
        