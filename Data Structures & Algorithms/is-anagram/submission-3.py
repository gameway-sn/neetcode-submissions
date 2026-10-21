class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs, ht = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hs[s[i]] = 1 + hs.get(s[i], 0)
            ht[t[i]] = 1 + ht.get(t[i], 0)
        
        print(hs, ht)
        
        if hs == ht:
            return True
        else:
            return False

        
            