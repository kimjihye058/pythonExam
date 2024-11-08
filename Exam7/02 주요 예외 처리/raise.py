class NotEvenNumberError(Exception):
    pass

def even_number_add(a, b):
    if a%2 != 0 or b%2 != 0:
        raise NotEvenNumberError        # 사용자가 정의한 예외를 활용
    return a+b

try:
    a = even_number_add(2, 2)
    print("결과 값 : ", str(a))
    b = even_number_add(4, 2)
    print("결과 값 : ", str(b))
    c = even_number_add(2, 1)
except NotEvenNumberError as e:
    print("짝수만 더할 수 있습니다.")