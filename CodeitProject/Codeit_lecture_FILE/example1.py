day_list = []
sales_list = []

with open('chicken.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(": ")

        day_list.append(line[0])
        sales_list.append(line[1])

print(day_list)
print(sales_list)

sum_days = len(day_list)
sum_sales = 0

for i in sales_list:
    sum_sales += int(i)

print(sum_sales)

print(sum_sales / sum_days)