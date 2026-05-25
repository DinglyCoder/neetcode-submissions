class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        stack = []

        pairs = [(p, s) for p, s in zip(position, speed)]

        pairs.sort()

        print(pairs)




        for p, s in pairs:
            time = (target - p) / s

            while (stack and stack[-1] <= time):
                # print(f"{i} pop {time} {stack[-1]}")
                stack.pop()
            
            stack.append(time)

    
        return len(stack)

