class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        max_len = 0
        max_freq = 0
        hash_map = dict()


        # most_common + k >= window_len


        while (r < len(s)):
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1
            max_freq = max(max_freq, hash_map[s[r]]) 

            print(f"r={r} and l={l} and max_freq={max_freq}")

            if (max_freq + k >= r - l + 1):
                print("1")
                max_len = max(max_len, r - l + 1)
            else:
                print("2") 
                while(l < r and max_freq + k < r - l + 1):
                    print("3")
                    hash_map[s[l]] = hash_map.get(s[l], 0) - 1
                    l += 1

            r += 1

        return max_len

