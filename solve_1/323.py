from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            uf.union(a, b)
        
        return uf.len
    
    
class UF:
    def __init__(self, n: int):
        self.parents = [-1 for i in range(n)]
        self.len = n
        
    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        a, b = min(a, b), max(a, b)
        self.parents[b] = a
        self.len -= 1

        
    def find(self, a: int) -> int:
        cur = a
        while True:
            if self.parents[cur] == -1:
                break
            else:
                cur = self.parents[cur]
        return cur
        
