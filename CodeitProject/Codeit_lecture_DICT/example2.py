# 사전 뒤집기

# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(old_dict):
    new_dict = {}  # 새로운 사전
    for key, value in old_dict.items():
        new_dict[value] = key

    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))