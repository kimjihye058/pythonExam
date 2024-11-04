# 구구단 정의
def gugudan(default=2):
    for i in range(1, 10):
        print(default, " * ", i, " = ", default*i)

gugudan(3)
gugudan()