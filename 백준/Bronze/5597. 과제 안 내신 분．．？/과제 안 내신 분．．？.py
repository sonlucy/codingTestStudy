# arr = [i+1 for i in range(30)]
# arr = [*range(1,31)]
arr = [int(input()) for i in range(28)]

for i in range(1,31):
  if i not in arr:
    print(i)

  # if a not in arr:print(a)
#     a=int(input())
#     if (1<= a <= 30):
#         arr.remove(a)
# print(min(arr))
# print(max(arr))

