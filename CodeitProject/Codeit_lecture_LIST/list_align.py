# 리스트 정렬 (sorted / sort)
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

new_list = sorted(numbers)
print(new_list)

print(numbers)  # 기존의 numbers 자체를 바꿔주는 것은 아님

numbers.sort(reverse=True)
print(numbers)