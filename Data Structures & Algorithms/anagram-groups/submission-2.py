from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cout = defaultdict(list)

        for i in range(len(strs)):
            temp = [0] * 26
            for c in strs[i]:
                temp[ord(c) - ord('a')] += 1
            
            cout[tuple(temp)].append(strs[i])
        
        return list(cout.values())