word=input()

# 첫번째 방법 #
#print(1 if word==word[::-1]
#     else 0)

# 두번째 방법 #
print(int(word==word[::-1]))