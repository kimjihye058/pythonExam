def multi_num(multi, start, end):   # multi의 배수를 구하는 함수
    result = []                     # 빈 리스트 생성
    for n in range(start, end):     # start부터 end-1까지 반복
        if n % multi == 0:          # multi의 배수인가?
            result.append(n)        # 그렇다면 list에 .append()
    return result                   # 함수 리턴

multi1 = multi_num(17, 1, 200)      
print("multi_num(17, 1, 200) : ", multi1)
print()
multi2 = multi_num(3, 1, 100)
print("multi_num(3, 1, 100) : ", multi2)