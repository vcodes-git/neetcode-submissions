class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: -x[0])
        stack = []

        for p, s in cars:
            time = (target - p)/s
            stack.append(time)
            if (len(stack) >= 2 and time <= stack[-2]):
                stack.pop()
        return len(stack)

