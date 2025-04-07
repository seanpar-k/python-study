import random

def generate_numbers(n):
    list_1 = []

    for i in range(0,n):
        num = random.randint(1, 45)

        if num not in list_1:
            list_1.append(num)
        else:
            continue

    return list_1

def draw_winning_numbers(n):
    num = random.randint(1, 45)
    list_2 = sorted(generate_numbers(n))
    while True:
        if num not in list_2:
            list_2.append(num)
            break
        else:
            continue

    return list_2

print(draw_winning_numbers(6))