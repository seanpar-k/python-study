ENG_list = []
KOR_list = []

with open("vocabulary.txt", "r", encoding = "utf-8") as f:
    for line in f:
        word_list = line.strip().split(": ")

        ENG_list.append(word_list[0])
        KOR_list.append(word_list[1])

Ans = '감자'

import random

while Ans != 'q':
    i = random.randint(0, 2)
    Ans = input("{}: ".format(KOR_list[i]))

    if Ans == ENG_list[i]:
        print("맞았습니다!")

    elif Ans != 'q' and Ans != ENG_list[i]:
        print("틀렸습니다. 정답은 {}입니다.".format(ENG_list[i]))

    else:
        break