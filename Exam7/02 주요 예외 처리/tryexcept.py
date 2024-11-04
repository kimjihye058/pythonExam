arr = [1, 2, 3]
try:
    print(arr[2])
    print(arr[3])       # [IndexError] 리스트에 접근하고 있으나 리스트 크기를 넘어서는 잘못된 첨자를 사용하고 있다.
except:
    print("리스트의 요소에 접근하지 못했습니다.")