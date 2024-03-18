N=int(input())
result=0

for N2 in range(1,N+1):
  digitSum=sum(map(int, str(N2))) #
  result=N2+digitSum
  if result==N:
    print(N2)
    break
  if N2==N:
    print(0)
    break
'''
def calculate_digit_sum(number):
    return sum(map(int, str(number)))

def find_number(N):
    for N2 in range(1, N + 1):
        digit_sum = calculate_digit_sum(N2)
        result = N2 + digit_sum
        if result == N:
            return N2
    return 0

N = int(input())
result = find_number(N)
print(result)
'''
