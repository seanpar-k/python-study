while True:
    ENG = input("영어 단어를 입력하세요: ")

    if ENG == 'q':
        break

    with open("vocabulary.txt", "a", encoding = "utf-8") as f:
        f.write(ENG)
        f.write(": ")

    KOR = input("한국어 뜻을 입력하세요: ")

    if KOR == 'q':
        break

    with open("vocabulary.txt", "a", encoding = "utf-8") as f:
        f.write(KOR)
        f.write("\n")

with open("vocabulary.txt", "r", encoding = "utf-8") as f:
    for line in f:
        print(line)