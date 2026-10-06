class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        ans = 0

        rollingSum = 0

        for num in nums:
            rollingSum += num
            required = rollingSum - k
            
            ans += prefixSums.get(required, 0)
            prefixSums[rollingSum] = prefixSums.get(rollingSum, 0) + 1
        
        return ans