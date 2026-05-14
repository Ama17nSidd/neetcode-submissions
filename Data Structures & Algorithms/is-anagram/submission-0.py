class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        
        for ch in t:
            if ch not in char_dict or char_dict[ch] < 1:
                return False
            char_dict[ch] -= 1
        
        return True
            

        