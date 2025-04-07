import random

def generate_numbers(n):
    list_1 = []

    for i in range(0,n):
        list_1.append(random.randint(1,45))   # 리스트 컴프리헨션 사용해서 더 간결하게 표현 가능

    return list_1
print(generate_numbers(6))

def draw_winning_numbers(n):

    list_2 = sorted(generate_numbers(n))
    list_2.append(random.randint(1,45))

    return list_2

print(draw_winning_numbers(6))

def count_matching_numbers(list_1, list_2):
    matching_num = 0
    list_2_copy = list_2.copy()

    for num in list_1:
        if num in list_2_copy:
            matching_num += 1
            list_2_copy.remove(num)

    return matching_num

count_matching_numbers([3, 1, 2, 1, 25, 8, 1], [1, 5, 3, 1, 2])

def check(list_1, list_2):
    list_2_a = list_2[:-1]
    list_2_bonus = list_2[-1]
    matching_num = count_matching_numbers(list_1, list_2_a)

    if matching_num == 6:
        print("10억")
    elif matching_num == 5 and list_2_bonus in list_1:
        print("5천만")
    elif matching_num == 5 and list_2_bonus not in list_1:
        print("100만")
    elif matching_num == 4:
        print("5만")
    elif matching_num == 3:
        print("5천")

check([1, 3, 5, 7, 8, 10], [1, 3, 5, 7, 9, 10, 8])