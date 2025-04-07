def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(0, len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] != solution[i] and guesses[i] in solution:    # 첫 번째 if문을 통과 못했다는건 앞의 !=는 이미 만족하고 있다는 것!
            ball_count += 1
        else:
            continue        # 어짜피 if문의 조건을 모두 훑고 내려왔으므로 없어도 다음 루프 실행됨.


    return strike_count, ball_count


# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)