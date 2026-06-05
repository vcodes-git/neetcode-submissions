class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for str in strs:
            temp = [0]*26
            for char in str: 
                idx = ord(char) - ord('a')
                temp[idx] += 1
            temp = tuple(temp)
            if temp in counts:
                counts[temp].append(str)
            else:
                counts[temp] = [str,]

        return list(counts.values())
        