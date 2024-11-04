arr = [1, 2, 3]
try:
    print(arr[4])       # [IndexError]
except IndexError as e: # e라는 이름의 객체로 접근하기 위해 as 키워드사용
    print(e)    # 예외와 관련된 내용 출력