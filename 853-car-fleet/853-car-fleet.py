class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i],speed[i]) for i in range(len(speed))]
        cars.sort(key=lambda x : x[0], reverse = True)
        print(cars)
        stack = []
        for p,s in cars:
            if stack and (target-p)/s <= (target-stack[-1][0])/stack[-1][1]:
                continue
            stack.append((p,s))
        return len(stack)