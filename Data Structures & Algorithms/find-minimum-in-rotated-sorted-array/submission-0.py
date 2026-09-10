class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        minnum = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                return min(minnum, nums[l])
            
            m = (l + r) // 2
            minnum = min(nums[m], minnum)

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minnum




            


        