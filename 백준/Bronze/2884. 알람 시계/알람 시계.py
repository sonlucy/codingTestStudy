H, M= map(int, input().split())

M=M-45 #45분 일찍
if (M<0):
    M=M+60
    H-=1
    if (H<0):
        H=23
print(H, M)