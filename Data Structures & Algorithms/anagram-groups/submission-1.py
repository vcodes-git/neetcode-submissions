class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            hot_enc = [0]* 26
            for letter in word:
                hot_enc[ord(letter) - ord('a')] += 1

            hmap[tuple(hot_enc)].append(word)
        
        return list(hmap.values())
            



        