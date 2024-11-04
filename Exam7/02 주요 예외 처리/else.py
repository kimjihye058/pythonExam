arr = [1, 2, 3]
try:
    print(arr[0])
    print(arr[1])
    print(arr[2])       # 예외 발생 x
except:
    print("예외 발생!")     # 예외가 발생하지 않아 실행 x
else:
    print("성공적으로 모든 코드를 실행!")       # try의 아무 이상이 없으면 else 블록 실행