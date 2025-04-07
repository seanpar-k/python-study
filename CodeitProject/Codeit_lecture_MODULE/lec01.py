from calculator import add, multiply # 모듈에서 원하는 함수만 가져오기

print(add(3, 2))


import calculator as calc # module 이름이 너무 길어 짧게 바꾸기

print(calc.add(2,5))
print(calc.multiply(3, 4))