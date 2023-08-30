#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque


class MyStack:
    
    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        move_l = len(self.q)
        self.q.appendleft(x)
        for i in range(move_l):
            self.q.appendleft(self.q.pop())
        

    def pop(self) -> int:
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
