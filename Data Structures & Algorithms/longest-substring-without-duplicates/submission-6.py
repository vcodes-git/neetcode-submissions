class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        subset = set()
        l = 0
        maxlen = 0

        for r in range(len(s)):
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[r])
            maxlen = max(r - l + 1, maxlen)
        return maxlen
        