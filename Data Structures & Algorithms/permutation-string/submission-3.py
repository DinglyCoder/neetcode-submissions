class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if (len(s1) > len(s2)):
            return False


        s1map = [0] * 26
        s2map = [0] * 26

        for c in s1:
            s1map[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            s2map[ord(s2[i]) - ord('a')] += 1

        print(f"{s1map}   -  {s2map}")

        l = 0
        r = len(s1)
        
        while r < len(s2):

            if s1map == s2map:
                return True

            s2map[ord(s2[l]) - ord('a')] -= 1
            l += 1
            s2map[ord(s2[r]) - ord('a')] += 1
            r += 1

            print(f"{s1map}   -  {s1map}")
        
        if s1map == s2map:
                return True
            

        return False

        




        