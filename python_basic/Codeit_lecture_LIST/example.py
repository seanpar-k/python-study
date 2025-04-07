# 04. 리스트 인덱싱 연습

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

i = 0
while i <=6:
    print(greetings[i])
    i += 1

# 05. 온도 단위 바꾸기
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]

print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

i = 0

while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)

    i += 1

print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력



