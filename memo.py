import bisect
from collections import defaultdict
import re
from typing import List

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

# 409 counter 
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        c = Counter(s)
        for k, v in c.items():
            result += (v // 2) * 2
            
        if not result == len(s) or len(s) == 1:
            result += 1
        return result

def div_mod():
    q, mod = divmod(10, 3)
    print(q, mod) # 3 1


from itertools import accumulate
def accum(nums: List[int]):
    list(accumulate(nums))
    
def letter_to_num():
    ord('c')-ord('a') # 2


def split_by_non_letters(text):
    pattern = r'[^a-zA-Z]+'
    return re.split(pattern, text)

# text = "Hello! This is a message."
# result = split_by_non_letters(text)
# print(result)  # Output: ['Hello', 'This', 'is', 'a', 'message']
