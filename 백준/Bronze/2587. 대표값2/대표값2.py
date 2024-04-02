
arr=[]
for _ in range(5):
  arr.append(int(input()))

print(sum(arr) // 5) 
print(sorted(arr)[2])

'''
sorted_arr = sorted(arr)
middle_index = len(arr) // 2
print(sorted_arr[middle_index])
'''