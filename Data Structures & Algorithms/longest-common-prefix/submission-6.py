class Solution(object):
    def longestCommonPrefix(self, strs):

        r = 0
        

        for i in range(min(len(s) for s in strs)):
            print(i)
            ch = strs[0][i]

            for s in strs:
                if s[i] != ch:
                    return strs[0][0:r]
            r+=1
            print(r)    
        
        return strs[0][0 : r]




