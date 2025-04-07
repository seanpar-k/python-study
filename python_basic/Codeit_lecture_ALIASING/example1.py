# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)

    for i in range(len(str_num)):
        total += int(str_num[i])   # 굳이 i를 이용 안해도 된다.
# for digit in str_num:
    # total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
sum_1 = 0
for i in range(1, 1001):
    sum_1 += sum_digit(i)

print(sum_1)