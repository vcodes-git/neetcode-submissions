class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in store and store[complement] != i: 
                return sorted([store[complement], i])
            else:
                store[nums[i]] = i
        
        