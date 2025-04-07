numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in numbers:
    print(numbers.index(i),i)

# 거듭제곱

for i in range(11):
    print(f"2^{i} = {2 ** i}")

for i in range(11):
    print("2^{} = {}".format(i, 2 ** i))

# 구구단

for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} * {y} = {x * y}")

# 피타고라스 삼조

for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    right = len(numbers) - left - 1

    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: {}".format(numbers))

people = ["승현", "종서", "소연", "선교", "보민"]

for a in range(len(people) // 2):
    b = len(people) - a - 1

    people[a], people[b] = people[b], people[a]

print("뒤집어진 리스트: " + str(people))


