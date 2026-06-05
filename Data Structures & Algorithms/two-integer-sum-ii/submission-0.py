class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        while True:
            twoSum = numbers[front] + numbers[back]
            if twoSum == target:
                return [front + 1, back + 1]
            if twoSum < target:
                front += 1
            else: 
                back -= 1

        