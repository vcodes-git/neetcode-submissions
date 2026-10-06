class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        subSet = set()
        maxlen = 0
        for r in range(0, len(s)):
            while s[r] in subSet:
                subSet.remove(s[l])
                l += 1
            
            subSet.add(s[r])
            maxlen = max(r-l+1, maxlen)
        return maxlen





        
 