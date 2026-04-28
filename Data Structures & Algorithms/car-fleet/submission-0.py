class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # fleetStack = []

        # while len(postion) > 0:
        #     for i in range(len(position)):
        #         next_pos = position[i] + speed[i]

        #         if next_pos in fleetStack:
        #             # remove from list 
        #         else
        #             fleetStack.append(next_pos)

        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



