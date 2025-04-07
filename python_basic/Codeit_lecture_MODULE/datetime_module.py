import datetime

pi_day = datetime.datetime(2020, 3, 14, 16, 8, 40)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

print(today - pi_day)
print(type(today - pi_day))

timedelta_1 = datetime.timedelta(days=5, hours=4, minutes=10, seconds=50)
print(today + timedelta_1)

# datetime 원하는 값 추출

print(today.year)
print(today.day)
print(today.month)

# datetime formating

print(today.strftime("%a %b %dth %Y"))