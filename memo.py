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
