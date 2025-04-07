def count_matching_numbers(numbers, winning_numbers):
    matching_num = 0

    for num in numbers:
        if num in winning_numbers:
            matching_num += 1

    return matching_num

print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))