class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = dict()

        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c) - ord('a')] = chars[ord(c) - ord('a')] + 1

            chars = str(chars)

            if chars not in ret:
                ret[chars] = [s]
            else:
                ret[chars].append(s)

        return list(ret.values())