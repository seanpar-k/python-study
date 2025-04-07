# split
my_str = '1. 2. 3. 4. 5. 6'
print(my_str.split(". "))  # .과 띄어쓰기를 기준으로 문자열을 구분해 리스트로 변환
print(type(my_str.split(". ")))

full_name = "Park, Jisung"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(last_name, first_name)

# spilt() 의 괄호 안에 아무 것도 넣지 않으면 공백을 기준으로 구분
print("     \n\n   2   \t   3  \n  5 7 11   \n  \n".split())
num = "     \n\n   2   \t   3  \n  5 7 11   \n  \n".split()
print(int(num[0]) + int(num[1]))

print(type(num[0]))