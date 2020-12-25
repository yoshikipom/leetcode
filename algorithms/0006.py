s = 'PAYPALISHIRING'
numRows = 4
n = len(s)
if numRows == 1:
    pass
    # return s

cycle = numRows * 2 - 2

result = ''
result += s[0:n:cycle]
for i in range(1, numRows - 1):
    tmp1 = s[i:n:cycle]
    tmp2 = s[cycle-i:n:cycle]
    if len(tmp1) == len(tmp2):
        for j in range(len(tmp1)):
            result += tmp1[j]+tmp2[j]
    else:
        for j in range(len(tmp2)):
            result += tmp1[j]+tmp2[j]
        result += tmp1[-1]
result += s[numRows-1:n:cycle]

print(result)
