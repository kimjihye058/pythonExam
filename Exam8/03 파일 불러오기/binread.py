import array

f = open("data.bin", "wb")

byte_arr = []
for i in range(0, 256):
    byte_arr.append(i)

data = bytes(byte_arr)

f.write(data)

f.close()

f = open("data.bin", "rb")      # 이진 데이터 파일을 이진 데이터 읽기(rb) 모드로 연다.
data = array.array("B")     # "B" 값을 전달하여 최소 0부터 255까지 숫자를 저장할 수 있는 리스트로 선언한다.
data.fromfile(f, 10)    # 이진 파일의 내용을 불러오기 위하여 fromflie 메소드를 사용한다.

for item in data:
    print(item, end=", ")

f.close()