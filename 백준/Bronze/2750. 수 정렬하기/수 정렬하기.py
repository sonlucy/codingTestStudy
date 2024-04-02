N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    if num not in arr:
        arr.append(num)

arr.sort()

for num in arr:
    print(num)
