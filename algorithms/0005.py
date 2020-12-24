s = input()

n = len(s)

result = ""
for i in range(n):
    l = i
    r = i
    while 0 <= l and r < n:
        if s[l] == s[r]:
            if len(result) < len(s[l:r+1]):
                result = s[l:r+1]
            l -= 1
            r += 1
        else:
            break


for i in range(n-1):
    if s[i] == s[i+1]:
        l = i
        r = i+1
        while 0 <= l and r < n:
            if s[l] == s[r]:
                if len(result) < len(s[l:r+1]):
                    result = s[l:r+1]
                l -= 1
                r += 1
            else:
                break


print(result)
