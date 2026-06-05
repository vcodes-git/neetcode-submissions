class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        # freq will hold lists of numbers. The index is the frequency.
        # Size is len(nums) + 1 because a number can appear at most len(nums) times.
        freq = [[] for i in range(len(nums) + 1)]
        
        # 1. Count frequencies (like we did in your previous prompt)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        # 2. Group numbers by their frequency
        for num, count in counts.items():
            freq[count].append(num)
            
        # 3. Gather results by reading the freq array backwards (highest frequency first)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res