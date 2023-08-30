#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
direction = [
    (-1, -1), 
    (-1, 0), 
    (-1, 1), 
    (0, -1), 
    (0, 0), 
    (0, 1), 
    (1, -1), 
    (1, 0), 
    (1, 1), 
]
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        h = len(img)
        w = len(img[0])
        for i in range(len(img)):
            img[i] = [None] +  img[i] + [None]
        img = [[None] * len(img[0])] + img + [[None] * len(img[0])]
        
        for row in img:
            print(*row)
        
        result = [[None for j in range(w)] for i in range(h)] 
        for i in range(1, h+1):
            for j in range(1, w+1):
                arr = []
                for dx, dy in direction:
                    if img[i+dx][j+dy] == None:
                        continue
                    arr.append(img[i+dx][j+dy])
                result[i-1][j-1] = sum(arr) // len (arr)
        return result
                    
        
        
        
# @lc code=end
