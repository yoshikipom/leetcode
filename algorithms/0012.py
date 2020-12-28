num = 3


def build(i, str_1, str_5, str_10):
    result = ''
    if i <= 3:
        result += str_1 * i
    elif i == 4:
        result += str_1 + str_5
    elif i <= 8:
        result += str_5 + str_1 * (i % 5)
    elif i == 9:
        result += str_1 + str_10
    return result


result = ''
result += build((num // 1000) % 10, 'M', '', '')
result += build((num // 100) % 10, 'C', 'D', 'M')
result += build((num // 10) % 10, 'X', 'L', 'C')
result += build(num % 10, 'I', 'V', 'X')

print(result)
