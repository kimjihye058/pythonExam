f = open("file.txt", "w")       # 텍스트 쓰기 접근 모드

f.write("hello")
f.write("\n")
f.write("world")

f.close()

f = open("file.txt", "a")       # 파일을 열면서 이어 붙이기 접근 모드

f.write("\n")
f.write("append")
f.close()