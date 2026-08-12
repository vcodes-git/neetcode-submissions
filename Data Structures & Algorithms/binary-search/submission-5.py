class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        i = 0
        while start < end:
            mid = (end + start)//2 
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid
            else: 
                return mid

        else:
            return -1 

        