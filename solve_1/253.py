import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # two pointer, endede, started
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key= lambda x: x[0])
        q = []
        result = 0
        for start, end in intervals:
            heapq.heappush(q, end)
            while q:
                tmp_end = heapq.heappop(q)
                if tmp_end <= start:
                    continue
                else:
                    heapq.heappush(q, tmp_end)
                    break
            result = max(result, len(q))
        return result
            
        
            
        
        
