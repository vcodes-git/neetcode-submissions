class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # -> (temp, i)
        out = [0] * len(temperatures)
        for i, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][0]:
                hitTemp, hitIndex = stack.pop()
                out[hitIndex] = i - hitIndex
            stack.append((temp, i))

        return out

        # BF 
        # out = []
        # for i, temp in enumerate(temperatures[:-1]):
        #     gt = 0
        #     for j, temp2 in enumerate(temperatures[i+1: ]):
        #         if temp2 > temp:
        #             gt = j + 1
        #             break
        #     out.append(gt)
        # out.append(0)
        # return out

        