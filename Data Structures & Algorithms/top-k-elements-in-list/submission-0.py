class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        repeat = {}
        for i in nums:
            repeat[i] = repeat.get(i, 0) + 1
        sorted_keys = sorted(repeat, key=repeat.get, reverse=True)
        return sorted_keys[:k]