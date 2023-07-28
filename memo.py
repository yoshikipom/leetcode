import bisect
from collections import defaultdict

# find value with log(n) time complexity (arr must be sorted)
def contains_value(arr, value):
    index = bisect.bisect_left(arr, value)
    return index < len(arr) and arr[index] == value

# default dict
def isSubsequence(self, s: str, t: str) -> bool:
    letter_indices_table = defaultdict(list)
    for index, letter in enumerate(t):
        letter_indices_table[letter].append(index)

# 401
# https://note.nkmk.me/python-zero-padding/
def zfill():
    s = '1234'
    print(s.zfill(8))    # 00001234
    print(type(s.zfill(8)))    # <class 'str'>

# 401
# bit string (e.g. "10111011") by using bin
# formt by using f"" can do zero padding
def readBinaryWatch(self, turnedOn: int) -> List[str]:
    output = []
    for h in range(12):
        for m in range(60):
            if bin(h).count('1') + bin(m).count('1') == turnedOn:
                output.append(f"{h}:{m:02d}")
    return output

# 461 count bit diff
x = 1
y = 4
bin(x ^ y).count('1') # -> 2 bits are not same.
