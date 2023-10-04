#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        if self.arr:
            min_so_far = min(self.arr[-1][1], val)
        else:
            min_so_far = val
        self.arr.append((val, min_so_far))
        

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
