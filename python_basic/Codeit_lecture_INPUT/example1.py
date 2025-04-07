import random

number = random.randint(1, 20)

for i in range(1, 5):
    x = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(5 - i)))

    if x > number:
        print("Down")
    elif x < number:
        print("Up")
    else:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(i))
        break
else:
    print("아쉽습니다. 정답은 {}였습니다.".format(number))


