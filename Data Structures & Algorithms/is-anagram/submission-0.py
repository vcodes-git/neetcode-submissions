class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for s_char, t_char in zip(s, t):
            s_dict[s_char] = s_dict.get(s_char, 0) + 1
            t_dict[t_char] = t_dict.get(t_char, 0) + 1
        
        return s_dict == t_dict
        