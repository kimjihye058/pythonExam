def sum(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value = sum_value + number
    return sum_value

result = sum(1, 3)
print("1 + 3 =", result)
print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))