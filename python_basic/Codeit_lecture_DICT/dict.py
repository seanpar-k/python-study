# 사전 (dictionary)
# key-value pair (키-값 쌍)

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(type(my_dictionary))

print(my_dictionary[3])

my_dictionary[9] = 81
print(my_dictionary)        # 순서 상관 없음, key가 꼭 정수형일 필요 없다

my_family = {
    'mom': '김송희',
    'dad': '박찬규',
    'me': '박종서'
}

print(my_family['mom'])

print(my_family.values())

print('박종서' in my_family.values())

print('최승현' in my_family.values())

for value in my_family.values():
    print(value)

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

for key, value in my_family.items():
    print(key, value)