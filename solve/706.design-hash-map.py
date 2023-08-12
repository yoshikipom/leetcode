#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
from typing import List


divisor = 769
def _hash(num: int) -> int:
    return num % divisor

class MyHashMap:

    def __init__(self):
        self.arr: List[List[int]] = [[] for i in range(divisor)]

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.arr[_hash(key)].append((key, value))
        

    def get(self, key: int) -> int:
        # print(self.arr)
        bucket = self.arr[_hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        # print('arr missing')
        return -1
        

    def remove(self, key: int) -> None:
        bucket = self.arr[_hash(key)]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
