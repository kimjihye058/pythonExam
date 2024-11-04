def hello(name, msg="안녕하세요"):
    print(name + "님, " + msg + "!")

hello("김철수", "오랜만이에요")
hello("이영희")     # 기본 인자 값이 없는 변수 순서가 기본 인자 값이 있는 변수보다 앞에 오게 한다.