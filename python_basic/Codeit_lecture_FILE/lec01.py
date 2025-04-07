with open('chicken.txt', 'r', encoding="utf-8") as f:  # 같은 directory 안에 있어 파일명으로 바로 인식 가능
    print(type(f))
    for line in f:
        print(line.strip())
# 현재 chicken.txt 파일이 인코딩 된 방식이 utf-8 임
# 내 컴퓨터가 읽으려는 방식은 CP949여서 오류 발생
# 따라서 encoding='utf-8' 을 덧붙여서 해결 가능

