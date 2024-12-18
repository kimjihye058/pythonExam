def min_max(*args):     # 숫자들 중에서 최솟값과 최곳값을 반환하는 함수
    min = args[0]       # 첫 번째 인수로 초기화
    max = args[0]
    for arg in args:    # 가변인수(숫자들) 하나씩 반복
        if min > arg:   # 숫자가 최솟값보다 작으면
            min = arg   # 그 숫자가 최솟값이 됨
        if max < arg:   # 숫자가 최댓값보다 크면
            min = arg   # 그 숫자가 최댓값이 됨
    return min, max     # 최솟값과 최댓값 리턴

print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최솟값:", min_value)
print("최솟값:", max_value)