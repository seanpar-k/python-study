# 리스트에서 값 존재 확인하기 (in 과 not in 을 이용하자)

primes = [2, 3, 5, 7, 11, 13]

print(7 in primes)
print(12 in primes)
print(12 not in primes)

# 리스트 안의 리스트 (Nested list)

grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

print(grades[0]) # 첫 번째 학생의 성적

print(grades[0] [2]) # 첫 번째 학생의 세 번째 시험 성적

# sort method

numbers = [5, 3, 7, 1]
numbers.sort()  # 새로운 리스트를 생성하지 않고 기존 numbers라는 함수를 정렬된 상태로 바꿔줌
print(numbers)

# reverse method

numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)  # 순서를 거꾸로 배열

# index method

members = ["js", "sy", "sg", "sh"]
print(members.index("sh"))  # list 안의 원소의 위치를 확인

# remove method

fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론", "파인애플"]
fruits.remove("파인애플")   # 가장 처음의 해당 원소만 삭제한다. 모든 "파인애플"을 삭제하지 않음.
print(fruits)