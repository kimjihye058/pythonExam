f = open("file.txt", "w")       # 파일을 쓰기 모드로 열기

try:
    f.write("Hello World")
    f.write(100)        # [TypeError] 문자열만 쓸 수 있으므로 숫자를 쓰고 있어 잘못된 자료형이다.
except TypeError:
    print("타입 예외 발생(100은 쓸 수 없음)")
finally:
    print("예외 여부와 상관 없이 무조건 실행")      # finally: 예외 발생 여부와 상관 없이 실행된다.
    f.close()       # 파일 닫는 처리