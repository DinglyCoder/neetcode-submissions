class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = dict()

        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            
            if tuple(chars) not in ret:
                ret[tuple(chars)] = [s]
            else:
                ret[tuple(chars)].append(s)

        return list(ret.values())