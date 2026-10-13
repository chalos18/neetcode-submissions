class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, speed) for pos, speed in zip(position, speed)], reverse=True)
        stack = []
        fleet = 0

        for pos, speed in cars:
            t = (target - pos)/speed
            if stack:
                t_top = (target - stack[-1][0])/stack[-1][1]
                if t <= t_top:
                    fleet+=1
                else:
                    stack.append((pos,speed))
            else:
                stack.append((pos,speed))
        return len(stack)
