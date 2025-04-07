# 리스트
numbers = [2, 3, 5, 7, 11, 13]    #list의 range를 생각하며 indexing
names = ["윤수", "혜린", "태호", "영훈"]

#indexing
print([names[0]])

num_1 = numbers[1]
num_3 = numbers[3]

print(num_1 + num_3)

print(numbers[-6])  # 5개의 요소가 있을 때 범위는 -6~-1 or 0~5

# list slicing
print(numbers[0:4])  # 0번 index에서부터 4개까지 slicing
print(numbers[-6:2])

new_list = numbers[:3]

numbers[0] = numbers[0] + numbers[1]
print(numbers)