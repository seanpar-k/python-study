# 07. 리스트 함수 활용하기

numbers = []
print(numbers)

numbers.append (1)
numbers.append (7)
numbers.append (3)
numbers.append (6)
numbers.append (5)
numbers.append (2)
numbers.append (13)
numbers.append (14)

print(numbers)

i = 0
while i < len (numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1

print(numbers)

numbers.insert(0, 20)

print(numbers)

numbers.sort (reverse = False)

print(numbers)