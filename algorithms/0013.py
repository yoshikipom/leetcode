result = 0

s = "LVIII"


def change(s, str_1, str_5, str_10):
    if str_1+str_10 in s:
        # 9
        return s.replace(str_1+str_10, str_5+str_1*4, 1)
    elif str_1+str_5 in s:
        # 4
        return s.replace(str_1+str_5, str_1*4, 1)
    else:
        return s


s = change(s, 'C', 'D', 'M')
# print(s)
s = change(s, 'X', 'L', 'C')
# print(s)
s = change(s, 'I', 'V', 'X')
# print(s)

result += 1000 * s.count('M')
result += 500 * s.count('D')
result += 100 * s.count('C')
result += 50 * s.count('L')
result += 10 * s.count('X')
result += 5 * s.count('V')
result += 1 * s.count('I')
print(result)
