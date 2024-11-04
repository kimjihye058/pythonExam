import os

data = os.listdir(".")      # listdir 함수를 이용하여 현재 디렉토리에 있는 파일과 디렉토리 목록을 data 변수에 리스트 형태로 저장
print(data)
for d in  data:
    print(d)
    print("is directory?: " + str(os.path.isdir(d)))
    print("is file?: " + str(os.path.isfile(d)))