def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1, 10):
        print(n, " x ", i, " = ", n*i)

if __name__ == "__main__":      # 메인 모듈로 실행될 경우 __name__ 내장 변수가 __main__으로 설정되는 것을 이용해 메인 모듈로 실행된 경우에만 gugudan(3) 함수가 호출
    gugudan(3)