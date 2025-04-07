ENG_list = []
KOR_list = []

with open("vocabulary.txt", "r", encoding = "utf-8") as f:
    for line in f:
        word_list = line.strip().split(": ")

        ENG_list.append(word_list[0])
        KOR_list.append(word_list[1])

i = 0

for Q in KOR_list:
    Ans = input("{}: ".format(Q))

    if Ans == ENG_list[i]:
        print("맞았습니다!\n")
        i += 1

    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(ENG_list[i]))
        i += 1

