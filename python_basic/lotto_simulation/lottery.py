import random


def generate_numbers(n):
    list_1 = []

    for i in range(0, n):
        num = random.randint(1, 45)

        if num not in list_1:
            list_1.append(num)
        else:
            continue

    return list_1

def draw_winning_numbers():
    num = random.randint(1, 45)
    list_2 = sorted(generate_numbers(6))
    while True:
        if num not in list_2:
            list_2.append(num)
            break
        else:
            continue

    return list_2

def count_matching_numbers(numbers, winning_numbers):
    matching_num = 0

    for num in numbers:
        if num in winning_numbers:
            matching_num += 1

    return matching_num

def check(numbers, winning_numbers):
    winning_numbers_a = winning_numbers[:-1]
    winning_numbers_bonus = winning_numbers[-1]
    matching_num = count_matching_numbers(numbers, winning_numbers_a)

    if matching_num == 6:
        return 1000000000
    elif matching_num == 5 and winning_numbers_bonus in numbers:
        return 50000000
    elif matching_num == 5 and winning_numbers_bonus not in numbers:
        return 1000000
    elif matching_num == 4:
        return 50000
    elif matching_num == 3:
        return 5000
    else:
        return 0