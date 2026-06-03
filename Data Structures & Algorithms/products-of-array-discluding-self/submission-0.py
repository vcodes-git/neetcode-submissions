class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Step 1: Populate output array with prefix products
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]
            
        # Step 2: Dynamically multiply suffix products walking backward
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix_prod   # Multiply current prefix by current suffix
            suffix_prod *= nums[i]     # Update the suffix tracker for the next element
            
        return output

        



        