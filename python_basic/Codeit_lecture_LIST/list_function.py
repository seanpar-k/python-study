# len
numbers = []
print(len(numbers)) # len은 length의 줄임말

# numbers.append
numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))

# del, insert
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[3]
print(numbers)

numbers.insert(4,37)    # append: 오른쪽 끝에 값 추가, insert: 원하는 곳에 추가
print(numbers)    # 4번 자리에 값 추가 후 기존 4번 자리의 값부터는 그 오른쪽에 써진다.

# round
numbers = [4.43, 2.22, 2.35, 7.21]

i = 0
while i < len(numbers):
    numbers[i] = round(numbers[i], 1)
    i += 1

print(numbers)