class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # maps value -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
                break

            seen[num] = i