class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        out = []
        for i, temp in enumerate(temperatures[:-1]):
            gt = 0
            for j, temp2 in enumerate(temperatures[i+1: ]):
                if temp2 > temp:
                    gt = j + 1
                    break
            out.append(gt)
        out.append(0)
        return out

        