# for 반복문

my_list = [2,3,5,7,11]

for number in my_list:
    print(number)  # 리스트의 처음부터 마지막까지 진행.

# range 함수의 필요성

for i in [1,2,3,4,5,6,7,8,9,10]:    # 만약 범위가 커진다면 리스트 작성 시 노가다 발생
    print(i)

# 파라미터 2개 버전, 1개 버전

start = 3
stop = 10
for i in range(start, stop):    # start 부터 stop - 1 까지의 범위
    print(i)

for i in range(stop):    # 0부터 stop - 1 까지의 범위
    print(i)

# 파라미터 3개 버전

# for i in range(start, stop, step)    # start 부터 stop - 1 까지의 범위, 간격은 step

for i in range(3, 17, 3):
    print(i)
