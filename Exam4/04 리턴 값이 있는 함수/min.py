def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number
    return min_value
result = min(1, 3)
print("min(1, 3) =", result)
print("min(0, 3, -11) =", min(0, 3, -11))