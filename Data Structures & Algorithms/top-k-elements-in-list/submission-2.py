class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        freq = [[] for _ in range(len(nums)+1)]
        
        for item in counts:
            freq[counts[item]].append(item)
        # print(counts.items())
        # print(freq)
        ret = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret


        