a, b = map(int, input().strip().split())

# 숫자 역순으로 만들기
reversed_a = int(str(a)[::-1])
reversed_b = int(str(b)[::-1])

# 큰 값 출력
print(max(reversed_a, reversed_b))
