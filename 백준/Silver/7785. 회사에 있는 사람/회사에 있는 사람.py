import sys

n = int(sys.stdin.readline().strip())
arr = set()  # 사용자 목록을 집합으로 관리 (중복 방지 및 삽입/삭제 O(1))

for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    if b == 'enter':
        arr.add(a)  
    elif b == 'leave':
        if a in arr:
            arr.remove(a)

sorted_users = sorted(arr, reverse=True)  
for user in sorted_users:
    print(user)