class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        rec = 0
        
        while l <= r:
            mid = (l + r)//2
            total = sum([math.ceil(pile / mid) for pile in piles])
            if total <= h:
                rec = mid
                r = mid - 1
            else:
                l = mid + 1
        return rec