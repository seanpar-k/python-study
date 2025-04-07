# 유사점

# indexing

alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])

# for 반복문

alphabets_list = ['s', 'e', 'a', 'n']
for alphabet in alphabets_list:
    print(alphabet)

alphabets_string = 'sean'
for alphabet in alphabets_string:
    print(alphabet)

# slicing

alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])

print(type(alphabets_list[0:5]))

alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])

print(type(alphabets_string[0:5]))   # 리스트와 문자열 모두 슬라이싱은 가능하지만 type은 서로 다르다.

# 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

str1 = '1234'
str2 = '5678'
str3 = str1 + str2
print(str3)

# len 함수

print(len(list3))

print(len(str3))

# 차이점

# mutable vs immutable

numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

name = 'sean'
print(name[0] == 's')
name[0] = 'S'   # 코드 오류 발생, 문자열 데이터 수정 불가!

