import random

def generate_numbers():
    list_1 = []
    num_1 = random.randint(0,9)
    list_1.append(num_1)

    # 2번째 번호 설정
    while True:
        num_2 = random.randint(0,9)

        if num_1 == num_2:
            continue

        else:
            list_1.append(num_2)
            break
    # 3번째 번호 설정
    while True:
        num_3 = random.randint(0, 9)

        if num_3 in list_1:
            continue

        else:
            list_1.append(num_3)
            break

    return list_1

print(generate_numbers())



