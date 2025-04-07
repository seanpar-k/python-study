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
        elif num_3 > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            numbers.append(num_3)
            break

    return numbers

print(take_guess())