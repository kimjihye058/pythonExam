import sys

def tri_area(width, height):
    return width * height * 1/2

def box_area(width, height):
    return width * height

def print_area(width, height):
    print("가로", width, "세로", height, "인 삼각형의 넓이 : ", tri_area(width, height))
    print("가로", width, "세로", height, "인 사각형의 넓이 : ", box_area(width, height))

if __name__ == "__main__":
    if len(sys.argv) == 3:      # sys.argv 리스트의 수를 확인, 가로, 세로가 반드시 입력되어야 해서 항목의 수가 3개인지 확인
        print_area(int(sys.argv[1]), int(sys.argv[2]))      # 두번째, 세번째 항목을 print_area() 함수의 매개 변수로 넘겨서 출력
    else:
        print("사용법 : python area3 가로 세로")