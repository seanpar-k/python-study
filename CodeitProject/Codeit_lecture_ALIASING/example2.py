# 문자열은 수정 불가능하므로 리스트로 변환하여 수정 이후 다시 문자열로 변환

def mask_security_number(security_number):
    list_num = list(security_number)

    for i in range(len(list_num)-4, len(list_num)):
        list_num[i] = '*'


    masked_num = ''.join(list_num)        # join 매소드 사용 -> 리스트를 문자열로 변환

    return masked_num

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

# 문자열 slicing 이용한 함수 정의

def mask_security_number(security_number):
    return security_number[:-4] + '****'

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
