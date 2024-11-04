# star 함수 정의

def star(a, *b):
    for i in range(len(b)):
        print(a*b[i])

star("음악", 3)
star("하트", 1, 2, 3)