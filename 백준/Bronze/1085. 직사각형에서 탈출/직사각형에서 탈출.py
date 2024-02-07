x,y,w,h=map(int, input().split())
# |x-w|, |y-h|, x, y 중에 최솟값을 출력하면 된다.
print( min(abs(x-w) ,abs(y-h) ,x ,y) )