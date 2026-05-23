class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            if s[r] not in seen:
                # add len
                max_len = max(max_len, r - l + 1)
                seen.add(s[r])
            else:
                # increment l
                while (l < r and s[l] != s[r]):
                    seen.discard(s[l])
                    l += 1
                l += 1
                seen.add(s[r])
            
        return max_len
