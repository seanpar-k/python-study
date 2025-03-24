alphabet_string = 'abcdefghij'

print(alphabet_string[0])
print(alphabet_string[-1])

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])

print(type(alphabet_string[4:]))

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:6])

str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

print(len(str_3))

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

print(len(list_3))

# 문자열과 리스트의 차이

numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

name = 'sean'
name[0] = 'P' # 문자열 수정 불가능 -> 오류 발생
print(name)