def solve(s):
    li = s.split()

    if len(li) == 0:
        return 0

    s = li[0]
    sign = 1
    if s[0] == '+' or s[0] == '-':
        if s[0] == '-':
            sign = -1
        s = s[1:len(s)]

    result = 0
    for i in range(len(s)):
        c = s[i]

        try:
            num = int(s[i])
            result = 10*result + num
            if sign * result < (-2 ** 31):
                return -2 ** 31
            elif (2 ** 31 - 1) < sign * result:
                return 2 ** 31 - 1
        except ValueError:
            return sign * result
    return sign * result


print(solve("42"))
print(solve("   -42"))
print(solve("4193 with words"))
print(solve("words and 987"))
print(solve("-91283472332"))
