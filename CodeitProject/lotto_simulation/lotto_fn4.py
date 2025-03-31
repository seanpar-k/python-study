def count_matching_numbers(numbers, winning_numbers):
    matching_num = 0

    for num in numbers:
        if num in winning_numbers:
            matching_num += 1

    return matching_num

def check(list_1, list_2):
    list_2_a = list_2[:-1]
    list_2_bonus = list_2[-1]
    matching_num = count_matching_numbers(list_1, list_2_a)

    if matching_num == 6:
        return 1000000000
    elif matching_num == 5 and list_2_bonus in list_1:
        return 50000000
    elif matching_num == 5 and list_2_bonus not in list_1:
        return 1000000
    elif matching_num == 4:
        return 50000
    elif matching_num == 3:
        return 5000
    else:
        return 0

numbers_test = [2, 4, 11, 14, 25, 40]
winning_numbers_test = [4, 12, 14, 28, 40, 41, 6]

print(check(numbers_test, winning_numbers_test))

numbers_test = [2, 4, 11, 14, 25, 40]
winning_numbers_test = [2, 4, 10, 11, 14, 40, 25]

print(check(numbers_test, winning_numbers_test))