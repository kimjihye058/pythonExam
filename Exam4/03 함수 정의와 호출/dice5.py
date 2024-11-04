import random

# 인자 값 - 주사위 여러 번 굴리게 하기
def rolling_dice(pip, repeat):
    for r in range(1, repeat+1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과", r, " : ", n)

rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)     # repeat 매개변수를 0 이하로 호출한 경우 반복이 동작하지 않는다.
rolling_dice(20, -3)