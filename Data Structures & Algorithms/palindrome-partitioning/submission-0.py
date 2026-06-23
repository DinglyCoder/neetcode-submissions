class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        running = []

        def dfs(previ, i, s, res, running):
            if i == len(s):
                total_elements = sum(map(len, running))
                if total_elements == len(s):
                    res.append(running.copy())
                return

            # don't partition here
            dfs(previ, i + 1, s, res, running)
            
            # partition here
            l = previ
            r = i
            palindrome = True
            print(f"test {l} and {r}")
            while l < r:
                if (s[l] != s[r]):
                    palindrome = False
                l += 1
                r -= 1
            if palindrome:
                print(f"palindrome at {i}")
                running.append(s[previ:i+1])
                dfs(i + 1, i + 1, s, res, running)
                running.pop()

            return

        dfs(0, 0, s, res, [])

        return res