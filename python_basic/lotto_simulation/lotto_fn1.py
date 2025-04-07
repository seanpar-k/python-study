import random

def generate_numbers(n):
    list_1 = []

    for i in range(0,n):
        num = random.randint(1,45)

        if num not in list_1:
            list_1.append(num)
        else:
            continue
        
    return list_1

print(generate_numbers(5))
print(generate_numbers(6))