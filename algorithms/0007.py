x = int(input())

str_x = str(abs(x))
result = int(str_x[::-1])
if x < 0:
    result = result * (-1)
if x < (-2 ** 31) or (2 ** 31 - 1) < x:
    result = 0

print(result)
