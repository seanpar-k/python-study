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

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    numbers = []
    while True:
        num_1 = int(input("1번째 숫자를 입력하세요: "))

        if num_1 > 9 or num_1 < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            numbers.append(num_1)
            break

    while True:
        num_2 = int(input("2번째 숫자를 입력하세요: "))

        if num_2 == num_1:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif num_2 > 9 or num_2 < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            numbers.append(num_2)
            break

    while True:
        num_3 = int(input("3번째 숫자를 입력하세요: "))

        if num_3 in numbers:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif num_3 > 9 or num_3 < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            numbers.append(num_3)
            break

    return numbers

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(0, len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:    # 첫 번째 if문을 통과 못했다는건 앞의 !=는 이미 만족하고 있다는 것!
            ball_count += 1

    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0

while True:
    GUESS = take_guess()
    strike_count, ball_count = get_score(GUESS, ANSWER)
    tries += 1
    print("{}S {}B".format(strike_count, ball_count))
    if strike_count == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
        break
