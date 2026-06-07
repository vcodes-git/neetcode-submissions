class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        start = intervals[0][0]
        end = intervals[0][1]
        out = []
        for i in intervals:
            if i[0] == start or i[0] <= end:
                end = max(end, i[1])
            
            else: 
                out.append([start, end])
                start, end = i[0], i[1]
        out.append([start, end])
        return out

            

        