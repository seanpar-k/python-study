x = 5
y = x
x = 3
print(x)
print(y)  # 5에 y라는 nametag이 붙었다고 생각.

x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)
print(y)

print(id(x))
print(id(y))

x = [2, 3, 5, 7, 11]
y = list(x)  # x라는 리스트의 값만 참조해 새로운 리스트를 생성.
y[2] = 4
print(x)
print(y)

print(id(x))
print(id(y))