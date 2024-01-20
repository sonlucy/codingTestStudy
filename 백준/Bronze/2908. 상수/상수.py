a, b = map(int, input().strip().split())

# %연산자 사용해 숫자 반대로
# 734 %10 -> 4, 734//10%10 ->3, 734//100%10 ->7
k=1; s=100; a1=0; b1=0
for i in range(3):
    a1+= a//k%10 *s
    b1+= b//k%10 *s
    k*=10
    s/=10

print(max(int(a1),int(b1)))