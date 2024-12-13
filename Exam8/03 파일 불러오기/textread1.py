f = open("text.txt", "w", encoding="utf8")

f.write("안녕하세요.")
f.write("\n")
f.write("반갑습니다.")
f.write("\n")

f.close()

# 파일 읽기

f = open("text.txt", "r", encoding="utf8")

line1 = f.readline()    # 한 줄씩 파일 읽기
print("Line 1: " + line1)
line2 = f.readline()
print("Line 2: " + line2)
line3 = f.readline()
print("line 3: " + line3)   # 두번째 줄 밖에 없기 때문에 마지막은 출력되지 않음

f.close()