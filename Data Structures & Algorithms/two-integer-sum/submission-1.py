class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)): 
            comp = target - nums[i]
            if comp in hashmap.keys():
                return [nums.index(comp), i]
            hashmap[nums[i]] = comp
             

        