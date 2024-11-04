f = open("hangul.txt", "w", encoding="utf8")        # 한글을 입력하고 싶다면 encoding 값을 지정해야 함

f.write("한글")
f.write("\n")
f.write("English")

f.close()