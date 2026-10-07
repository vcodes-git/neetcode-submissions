class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curSum = 0
        minLen = math.inf
        cond = False
        for r in range(len(nums)):
            curSum += nums[r]
            # print(curSum)
            while curSum >= target:
                cond = True
                curSum -= nums[l]
                l += 1
                # print("inloop", curSum, "l =", l, "r =", r)
                # print("minLen", minLen, r - l + 1)
                minLen = min(minLen, r - l +2)
        
        return minLen if cond else 0

        