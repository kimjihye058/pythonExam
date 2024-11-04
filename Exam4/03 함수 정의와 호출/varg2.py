def p(*args):
    str = ""
    for a in args:
        str = str + a
    print(str)
p("하트")
p("하트", "음악")
p("하트", "음악", "클로버", "스페이드")
