def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)

p(",", 3, "하트", "음악")
p("별", 2, "하트", "음악", "클로버")
p("_", 3, "하트", "음악", "클로버", "스페이스")