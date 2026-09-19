class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        rep = {}
        for num in nums:
            rep[num] = rep.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in rep.items():
            bucket[value].append(key)

        output = []
        # Walk backward from highest possible frequency down to 1
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                output.append(num)
                if len(output) == k:
                    return output

        return output