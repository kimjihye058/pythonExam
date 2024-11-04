import random

# 인자 값 - 주사위 눈 수 조정
# pip - 주사위의 눈을 의미
def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과 : ", n)

rolling_dice(4)