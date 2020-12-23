s = input()

result = 0
count = 0
used = set()

l = 0
r = 0
n = len(s)
while l < n and r < n:
    if s[r] in used:
        used.remove(s[l])
        l += 1
    else:
        used.add(s[r])
        r += 1
        result = max(result, r - l)
print(result)
